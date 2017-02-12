import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pin = 18
GPIO.setup(pad_pin, GPIO.IN)

while True:
    pad_pressed = GPIO.input(pad_pin)
    if pad_pressed:
        print("touched!")

    time.sleep(0.1)
