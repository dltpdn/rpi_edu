import RPi.GPIO as GPIO

PIN_IN = 18
PIN_LED1, PIN_LED2 = 23, 24
old, val = -1, 0
state = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN)
GPIO.setup(PIN_LED1, GPIO.OUT)
GPIO.setup(PIN_LED2, GPIO.OUT)
    
try:
    GPIO.output(PIN_LED1, True)
    while True:
        val = GPIO.input(PIN_IN)
        if old != val :
            print(val)
            old = val
            if val == 0:
                GPIO.output(PIN_LED1, state)
                GPIO.output(PIN_LED2, not state)
                state = not state 
finally:
    GPIO.cleanup()