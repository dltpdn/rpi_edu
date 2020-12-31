# Notice!! Run with sudo
import wiringpi as wpi
PIN_LED = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_LED, wpi.PWM_OUTPUT)

while True:
	for i in range(0, 1024):
		wpi.pwmWrite(PIN_LED, i)
		wpi.delay(1)
	for i in range(1024, -1, -1):
		wpi.pwmWrite(PIN_LED, i)
		wpi.delay(1)
