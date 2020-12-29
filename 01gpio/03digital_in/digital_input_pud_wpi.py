import wiringpi as wpi

PIN = 18
wpi.wiringPiSetupGpio()
wpi.pinMode(PIN, wpi.INPUT)
wpi.pullUpDnControl(PIN, wpi.PUD_UP)
#wpi.pullUpDnControl(PIN, wpi.PUD_DOWN)
old_val = -1
while True:
	val = wpi.digitalRead(PIN)
	if val != old_val:
		old_val = val
		print(val)
