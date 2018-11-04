import time
import RPi.GPIO as GPIO

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pad_pin, GPIO.IN)

while True:
    pad_pressed = GPIO.input(pad_pin)
    if pad_pressed:
        print("touched!")

    time.sleep(0.1)
