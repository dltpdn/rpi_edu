import RPi.GPIO as GPIO

PIN_SW = 18
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_SW, GPIO.IN)
    
    while True:
        print(GPIO.input(PIN_SW))
finally:
    GPIO.cleanup()
