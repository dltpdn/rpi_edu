'''
Created on Oct 21, 2016

@author: rainer
'''
import RPi.GPIO as GPIO 
import time


PIR_PIN = 18
SERVO_PIN  = 25
pad_pin = 5

def main():
    val = -1
    delay = 3
    print('Mission-1 started.(delay time: %d)' %delay)
    for x in range(delay, 0, -1):
        time.sleep(1)
        print('Waiting.. ', x)
    try:    
        setup()
        p = GPIO.PWM(SERVO_PIN,100)
        p.start(5)
        p.ChangeDutyCycle(5)
        while True:
            read = GPIO.input(PIR_PIN)
            if read == 0:
                print(time.strftime("%Y%m%d-%H%M%S"), "No intruder")
            else :
                print(time.strftime("%Y%m%d-%H%M%S"), "Intruder dectected")
                while True:
                    pad_pressed = GPIO.input(pad_pin)
                    if pad_pressed:
                        print(("pressed! - " + time.strftime("%Y%m%d-%H%M%S")))
                        p.ChangeDutyCycle(15) #+90 degree
                        time.sleep(3)
                        p.ChangeDutyCycle(5)
                        break;
                    time.sleep(0.1)
    finally:
        GPIO.cleanup()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    GPIO.setup(pad_pin, GPIO.IN)

if __name__ == '__main__':
    main()
    pass