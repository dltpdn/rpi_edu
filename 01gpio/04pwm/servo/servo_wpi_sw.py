import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.OUTPUT)
wpi.softPwmCreate(pin, 5, 50) # 1000/50=20ms

while True:
	answer = input("1:-90, 2:0, 3: +90 > ")
	if answer =='1':
		wpi.softPwmWrite(pin, 2.5) # 0.5/20 = 0.025(2.5%)
	elif answer == '2':
		wpi.softPwmWrite(pin, 7.5) # 1.5/20 = 0.075(7.5%)
	else:
		wpi.softPwmWrite(pin, 12.5) #2.5/20 = 0.125(12.5%)
