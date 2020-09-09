import ctypes
import time

gpio = ctypes.CDLL('./led_register.so')

gpio.init()
gpio.setOut(18)

for i in range(10):
    print("LED On.")
    gpio.output(18, 1)
    time.sleep(0.5)
    
    print("LED Off.")
    gpio.output(18, 0)
    time.sleep(0.5)
