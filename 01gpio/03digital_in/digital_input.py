import RPi.GPIO as GPIO

pin = 18
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    
    while True:
        print GPIO.input(pin)
finally:
    GPIO.cleanup()
