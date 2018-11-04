import RPi.GPIO as GPIO

PIN_FAN = 18

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_FAN, GPIO.OUT)
    
    while True:
        val = eval(input("1:on, 0:off > "))
        GPIO.output(PIN_FAN, val)
finally:
    print('clean up')
    GPIO.cleanup()
