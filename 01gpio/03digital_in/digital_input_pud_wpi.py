import wiringpi as wpi

pin = 18;
wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.INPUT)
wpi.pullUpDnControl(pin, wpi.PUD_DOWN)

while True:
	print wpi.digitalRead(pin)
