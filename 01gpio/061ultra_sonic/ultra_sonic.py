import RPi.GPIO as GPIO 
import time

PIN_TRIG = 18
PIN_ECHO = 23 

dist, old_dist = 0,0
start_time = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_TRIG, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(PIN_TRIG, True)
        time.sleep(0.00001)  # 10us
        GPIO.output(PIN_TRIG, False)
        while GPIO.input(PIN_ECHO) == 0:
            pass
        start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pass
        travel_time = time.time() - start_time
        dist = travel_time * 17160 #34321/2
        dist = round(dist)
        if dist != old_dist:
            old_dist = dist
            print(f'Distance:{dist}cm')
        time.sleep(0.01)
finally:
    print('Clean up')
    GPIO.cleanup()                
