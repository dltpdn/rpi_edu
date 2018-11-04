import wiringpi as wpi

PIN_SW = 18;
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_SW, wpi.INPUT)
wpi.pullUpDnControl(PIN_SW, wpi.PUD_DOWN)

while True:
	print(wpi.digitalRead(PIN_SW))
