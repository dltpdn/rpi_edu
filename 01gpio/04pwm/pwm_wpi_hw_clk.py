import wiringpi as wpi
pin = 18;

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.OUTPUT)

wpi.pwmSetClock(1920)
wpi.pwmSetRange(1000)

while True:
	for i in range(0, 1001):
		wpi.pwmWrite(pin, i)
		wpi.delay(1)
	for i in range(1000, -1, -1):
		wpi.pwmWrite(pin, i)
		wpi.delay(1)
