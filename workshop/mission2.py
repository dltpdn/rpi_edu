'''
Created on Oct 21, 2016

@author: rainer
'''

import RPi.GPIO as GPIO 
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11


def main():
    max_temp = 25
    max_humi = 40
    
    dht_pin = 7
    fan_pin = 6
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(fan_pin, GPIO.OUT)
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
            if humidity is not None and temperature is not None:
                print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
                if temperature > max_temp or humidity > max_humi:
                    GPIO.output(fan_pin, True)
                else:
                    GPIO.output(fan_pin, False)
            else:
                print("Failed to get reading.")
                GPIO.output(fan_pin, False)
    finally:
        print('clean up')
        GPIO.cleanup()    
    
    
if __name__ == '__main__':
    main()
    pass






# GPIO23 (pin no: #16)


