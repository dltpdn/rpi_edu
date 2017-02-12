import RPi.GPIO as GPIO
import time


try:
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    val = -1
    while True:
        read = GPIO.input(pin)
        if read != val:
            val = read
            print  val == 0 and 'no IR' or 'IR detected'
        #time.sleep(0.1)
finally:
    print "clean up."
    GPIO.cleanup()
