import RPi.GPIO as GPIO
import time

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
val = -1

try:
    while True:
        read = GPIO.input(PIN)
        if read != val:
            val = read
            print(val == 0 and 'no IR' or 'IR detected')
        #time.sleep(0.1)
finally:
    print("clean up.")
    GPIO.cleanup()
