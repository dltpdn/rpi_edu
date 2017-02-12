import RPi.GPIO as GPIO
import time

try:
    pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    pwm = GPIO.PWM(pin, 100)
    pwm.start(0)

    while True:
        for i in range(0, 101):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.05)
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.05)
finally:
    pwm.stop()
    GPIO.cleanup()
