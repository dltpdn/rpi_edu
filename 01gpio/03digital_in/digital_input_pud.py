import RPi.GPIO as GPIO

PIN_SW = 18
try:
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(PIN_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:
        print(GPIO.input(PIN_SW))
finally:
    GPIO.cleanup()
