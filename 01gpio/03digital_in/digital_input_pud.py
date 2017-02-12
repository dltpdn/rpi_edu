import RPi.GPIO as GPIO

pin = 18
try:
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:
        print GPIO.input(pin)
finally:
    GPIO.cleanup()
