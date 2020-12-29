import wiringpi as wpi
import time

PIN_IN = 18
PIN_LED1, PIN_LED2 = 23, 24
old, val = -1, 0
state = False
bounce_time = 0.100 # 100ms
last_time = 0
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_IN, wpi.INPUT)
wpi.pinMode(PIN_LED1, wpi.OUTPUT)
wpi.pinMode(PIN_LED2, wpi.OUTPUT)
    
wpi.digitalWrite(PIN_LED1, True)

while True:
    val = wpi.digitalRead(PIN_IN)
    if old != val :
        print(val)
        old = val
        if val == 0:
            if (time.time() - last_time) > bounce_time:
                wpi.digitalWrite(PIN_LED1, state)
                wpi.digitalWrite(PIN_LED2, not state)
                state = not state 
            last_time = time.time()
