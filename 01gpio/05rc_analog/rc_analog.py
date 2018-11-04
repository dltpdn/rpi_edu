import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_CHARGE = 18
PIN_MEASURE = 23

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(PIN_CHARGE, GPIO.IN) #lock charging
    GPIO.setup(PIN_MEASURE, GPIO.OUT)
    GPIO.output(PIN_MEASURE, False) #making GND, discharge
    time.sleep(0.1) #waiting for discharge
    
    GPIO.setup(PIN_MEASURE, GPIO.IN) #switching GND to measuring pin
    GPIO.setup(PIN_CHARGE, GPIO.OUT) #making charge
    count = 0                       #reset counter
    GPIO.output(PIN_CHARGE, True)  #start charging
    while not GPIO.input(PIN_MEASURE):  #until recognize
        count = count + 1           #accumulate count
    print(count)
