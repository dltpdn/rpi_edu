import wiringpi as wpi
PIN_LED = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_LED, wpi.OUTPUT)
wpi.softPwmCreate(PIN_LED, 0, 100)

while True:
	for i in range(0,101): 
		wpi.softPwmWrite(PIN_LED, i)
		wpi.delay(10)
	
	for i in range(100,-1, -1):
		wpi.softPwmWrite(PIN_LED, i)
		wpi.delay(10)
