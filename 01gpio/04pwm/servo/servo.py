import RPi.GPIO as GPIO
import time

pin = 18
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin,100)
    pwm.start(5)
    while True:
        val = raw_input('1:-90, 2:0, 3:+90 > ')
        if val == '1':
            pwm.ChangeDutyCycle(5) #-90degree
        elif val == '2':
            pwm.ChangeDutyCycle(15) #0 dgree
        else :
            pwm.ChangeDutyCycle(25) #+90 degree
finally:
    pwm.stop()
    GPIO.cleanup()
