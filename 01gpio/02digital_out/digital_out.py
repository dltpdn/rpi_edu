import RPi.GPIO as GPIO

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
print(f'#{PIN} is set to OUTPUT.')
try:
    while True:
        val = input("1:on, 0:off > ")
        if val == '0':
            GPIO.output(PIN, GPIO.LOW)
            print('Off')
        elif val == '1':
            GPIO.output(PIN, GPIO.HIGH)
            print('On')
        else:
            break
finally:
    GPIO.cleanup()
    print('clean up and exit.')
    
