import wiringpi as wpi
import time
pin = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.INPUT)

def isr():
	print wpi.digitalRead(pin)

wpi.wiringPiISR(pin, wpi.INT_EDGE_BOTH, isr);

while True:
	time.sleep(100)
