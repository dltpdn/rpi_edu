import RPi.GPIO as GPIO

try:
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    val = -1
    while True:
        read = GPIO.input(pin)
        if read != val:
            val = read
            print 'dark' if val == 0 else 'light'
finally:
    print "clean up."
    GPIO.cleanup()
