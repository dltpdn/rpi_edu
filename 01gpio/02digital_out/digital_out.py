import RPi.GPIO as GPIO

fan_pin = 18

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT)
    
    while True:
        val = eval(input("1:on, 0:off > "))
        GPIO.output(fan_pin, val)
finally:
    print('clean up')
    GPIO.cleanup()
