import wiringpi as wpi
import time

PIN_SW = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_SW, wpi.INPUT)

def isr():
	print(wpi.digitalRead(PIN_SW))

wpi.wiringPiISR(PIN_SW, wpi.INT_EDGE_BOTH, isr);

while True:
	time.sleep(100)
