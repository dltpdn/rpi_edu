import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.OUTPUT)
wpi.softPwmCreate(pin, 5, 100);

while True:
	answer = raw_input("1:-90, 2:0, 3: +90 > ")
	if answer =='1':
		wpi.softPwmWrite(pin, 5)
	elif answer == '2':
		wpi.softPwmWrite(pin,15)
	else:
		wpi.softPwmWrite(pin, 25)
