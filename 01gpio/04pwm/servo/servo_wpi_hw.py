import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.PWM_OUTPUT)
wpi.pwmSetMode(wpi.PWM_MODE_MS)
wpi.pwmSetClock(1920)
wpi.pwmSetRange(100)

while True:
	answer = raw_input("1:-90, 2:0, 3: +90 > ")
	if answer =='1':
		wpi.pwmWrite(pin, 5)
	elif answer == '2':
		wpi.pwmWrite(pin,15)
	else:
		wpi.pwmWrite(pin, 25)
