import wiringpi as wpi
import time

PIN = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN, wpi.INPUT)

def isr():
	print(f'edge both :{wpi.digitalRead(PIN)}')

wpi.wiringPiISR(PIN, wpi.INT_EDGE_BOTH, isr)

while True:
	time.sleep(100)
