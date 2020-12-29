import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
# channel = GPIO.wait_for_edge(18, GPIO.RISING, timeout=5000)
# if channel is None:
#     print('Timeout occurred')
# else:
#     print('Edge detected on channel', channel)

def rising(channel):
    print(f'Rising Edge #{channel}') 
def falling(channel):
    print(f'Falling Edge #{channel}') 
def isr(channel):
    print(f'Both Edge #{channel}, {GPIO.input(channel)}') 

#GPIO.add_event_detect(18, GPIO.RISING, callback=rising, bouncetime=100)
#GPIO.add_event_detect(18, GPIO.FALLING, callback=falling, bouncetime=100)
GPIO.add_event_detect(18, GPIO.BOTH, callback=isr, bouncetime=100)
while True:
    time.sleep(100)