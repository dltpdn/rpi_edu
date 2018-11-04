import RPi.GPIO as GPIO 
import time

PIN_TRIG = 18
PIN_ECHO = 23 

distance = 0
start_time = 0
end_time=0

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_TRIG, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    
    while True:
        GPIO.output(PIN_TRIG, False)
        time.sleep(0.2)     #wait for being ready
        GPIO.output(PIN_TRIG, True)
        time.sleep(0.00001)  #set HIGH for 10us
        GPIO.output(PIN_TRIG, False)
        while GPIO.input(PIN_ECHO) == 0:
            start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            end_time = time.time()
        travel_time = end_time - start_time;
        distance = travel_time * 17160 #34321/2
        distance = round(distance, 2)
        print('Distance:%dcm' %distance)
finally:
    print('Clean up')
    GPIO.cleanup()                
