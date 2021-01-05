import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_CHARGE = 18
PIN_MEASURE = 23

GPIO.setmode(GPIO.BCM)

while True:
    # for discharge
    GPIO.setup(PIN_CHARGE, GPIO.IN) 
    GPIO.setup(PIN_MEASURE, GPIO.OUT)
    GPIO.output(PIN_MEASURE, False) 
    time.sleep(0.1) 
    
    # for charging and measuring
    GPIO.setup(PIN_MEASURE, GPIO.IN) 
    GPIO.setup(PIN_CHARGE, GPIO.OUT) 
    count = 0                       
    GPIO.output(PIN_CHARGE, True)  
    while not GPIO.input(PIN_MEASURE):  
        count = count + 1           
    print(count)
