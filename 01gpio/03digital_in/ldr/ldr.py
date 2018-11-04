import RPi.GPIO as GPIO

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
val = -1
try:
    while True:
        read = GPIO.input(PIN)
        if read != val:
            val = read
            print('dark' if val == 0 else 'light')
finally:
    print("clean up.")
    GPIO.cleanup()
