import RPi.GPIO as GPIO

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
old_val = -1
try:
    while True:
        val = GPIO.input(PIN)
        if val != old_val:
            old_val = val
            print(val)
finally:
    GPIO.cleanup()
