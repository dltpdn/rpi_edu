import RPi.GPIO as GPIO
import time

PIN_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
    
for i in range(10):
    GPIO.output(PIN_LED, True)
    print("Led on")
    time.sleep(0.5)
    GPIO.output(PIN_LED, False)
    print("Led off")
    time.sleep(0.5)
GPIO.cleanup()
