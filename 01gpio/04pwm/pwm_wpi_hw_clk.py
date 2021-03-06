# Notice!! Run with sudo
import wiringpi as wpi
PIN_LED = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_LED, wpi.PWM_OUTPUT)

wpi.pwmSetClock(1920) # 19,200,000/1,920 = 10,000
wpi.pwmSetRange(100) # 10,000 / 100 = 100Hz
while True:
	for i in range(0, 101):
		wpi.pwmWrite(PIN_LED, i)
		wpi.delay(10)
	for i in range(100, -1, -1):
		wpi.pwmWrite(PIN_LED, i)
		wpi.delay(10)
