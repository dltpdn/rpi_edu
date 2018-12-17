# run with sudo!!
import wiringpi as wpi
PIN_SERVO = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_SERVO, wpi.PWM_OUTPUT)

wpi.pwmSetMode(wpi.PWM_MODE_MS)
wpi.pwmSetClock(384)	#19.2MHz / 384 = 50000Hz = 50KHz(0.02ms)
wpi.pwmSetRange(1000) # 0.02ms * 1000 = 20ms, 50KHz / 1000 = 50Hz

while True:
	answer = input("1:-90, 2:0, 3: +90 > ")
	if answer =='1':
		wpi.pwmWrite(PIN_SERVO, 25)	# 25 * 0.02ms = 0.5ms
	elif answer == '2':
		wpi.pwmWrite(PIN_SERVO, 75)	# 75 * 0.02ms = 1.5ms
	else:
		wpi.pwmWrite(PIN_SERVO, 125)	# 125 * 0.02ms = 2.5ms 
