import RPi.GPIO as GPIO

PIN_IN = 18
PIN_OUT = 23
old, val = -1, 0
state = False
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_IN, GPIO.IN)
    GPIO.setup(PIN_OUT, GPIO.OUT)
    
    while True:
        val = GPIO.input(PIN_IN)
        if old != val :
            print(val)
            old = val
            if val == 0:
                state = not state 
            GPIO.output(PIN_OUT, state)
finally:
    GPIO.cleanup()
