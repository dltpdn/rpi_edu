import RPi.GPIO as GPIO
import time


led_pin = 18
    
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    
    while True:
        GPIO.output(led_pin, True)
        time.sleep(0.5)
        GPIO.output(led_pin, False)
        time.sleep(0.5)
finally:
    print 'clean up'
    GPIO.cleanup()
