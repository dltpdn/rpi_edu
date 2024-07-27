import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PINS = [12, 16, 20, 21]
cnt = 0
steps = 32*64 #31:1cycle, 1:64 ratio

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)

seq = [[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]]        
try:
    while True:
        for i in range(4):
            for j in range(4):
                pin = PINS[j]
                if seq[i][j] == 1:
                    GPIO.output(pin, True)
                else:
                    GPIO.output(pin, False)
            time.sleep(0.01)
            cnt +=1

        if cnt == steps:
            print("steps", steps)
            break
        
finally:
    GPIO.cleanup()