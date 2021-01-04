import RPi.GPIO as GPIO
import time

PIN_SERVO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SERVO, GPIO.OUT)
pwm = GPIO.PWM(PIN_SERVO,50)  # 50Hz, 1Period = 20ms
pwm.start(7.5)

try:
    while True:
        val = input('1:-90, 2:0, 3:+90, 9:Quit> ')
        if val == '1':
            #pwm.ChangeDutyCycle(2.5) #-90degree, 20ms * 2.5% = 0.5ms 
            pwm.ChangeDutyCycle(5) #-90degree, 20ms * 5% = 1ms 
        elif val == '2':
            pwm.ChangeDutyCycle(7.5) #0degree, 20ms*7.5% = 1.5ms
        elif val == '3':
            #pwm.ChangeDutyCycle(12.5) #+90degree, 20ms*12.5% = 2.5ms
            pwm.ChangeDutyCycle(10) #+90degree, 20ms*10% = 2ms
        elif val == '9' :
            break
finally:
    pwm.stop()
    GPIO.cleanup()
