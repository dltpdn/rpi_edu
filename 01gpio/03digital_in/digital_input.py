import RPi.GPIO as GPIO

PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
old_val = -1
try:
    while True:
        val = GPIO.input(PIN)
        if val != old_val:
            old_val = val
            print(val)
finally:
    GPIO.cleanup()
