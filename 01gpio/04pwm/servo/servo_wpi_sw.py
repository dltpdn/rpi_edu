import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.OUTPUT)
wpi.softPwmCreate(pin, 5, 200) #1pulse = 0.1ms(100us), 50Hz = 20ms, 20ms/0.1ms= 200(50Hz)

while True:
	answer = input("1:-90, 2:0, 3: +90 > ")
	if answer =='1':
		wpi.softPwmWrite(pin, 5) # 5 * 0.1ms = 0.5ms
	elif answer == '2':
		wpi.softPwmWrite(pin, 15) # 15*0.1ms = 1.5ms
	else:
		wpi.softPwmWrite(pin, 25) # 25*0.1ms = 2.5ms