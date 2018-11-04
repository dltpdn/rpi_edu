import RPi.GPIO as GPIO 
import time
from datetime import datetime

PIN_PIR = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_PIR, GPIO.IN)
val = -1

try:
    while True:
        read = GPIO.input(PIN_PIR)
        if val != read: 
            val = read
            if val== 0:
                print("No intruder")
            elif val == 1:
                print("Intruder dectected")
        time.sleep(0.5)
finally:
    print('clean up')
    GPIO.cleanup() 
