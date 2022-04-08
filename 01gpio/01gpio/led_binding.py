'''
Before running this code 
you should compile led_register.c file 
as led_register.so file.
$ gcc led_register.c -o led_register.so -shared
'''

import ctypes
import time

gpio = ctypes.CDLL('./led_lib.so')

gpio.init()
gpio.setOut(18)

for i in range(5):
    print("LED On.")
    gpio.output(18, 1)
    time.sleep(0.5)
    
    print("LED Off.")
    gpio.output(18, 0)
    time.sleep(0.5)
