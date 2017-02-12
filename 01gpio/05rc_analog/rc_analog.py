import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin_charge = 18
pin_measure = 23

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(pin_charge, GPIO.IN) #lock charging
    GPIO.setup(pin_measure, GPIO.OUT)
    GPIO.output(pin_measure, False) #making GND, discharge
    time.sleep(0.1) #waiting for discharge
    
    GPIO.setup(pin_measure, GPIO.IN) #switching GND to measuring pin
    GPIO.setup(pin_charge, GPIO.OUT) #making charge
    count = 0                       #reset counter
    GPIO.output(pin_charge, True)  #start charging
    while not GPIO.input(pin_measure):  #until recognize
        count = count + 1           #accumulate count
    print count
