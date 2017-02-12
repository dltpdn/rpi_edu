import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.OUTPUT)
wpi.softPwmCreate(pin, 0, 100)

while True:
	for i in range(0,101): 
		wpi.softPwmWrite(pin, i)
		wpi.delay(10)
	
	for i in range(100,-1, -1):
		wpi.softPwmWrite(pin, i)
		wpi.delay(10)
