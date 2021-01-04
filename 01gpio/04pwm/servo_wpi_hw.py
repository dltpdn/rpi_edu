# run with sudo!!
import wiringpi as wpi
PIN_SERVO = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(PIN_SERVO, wpi.PWM_OUTPUT)

wpi.pwmSetMode(wpi.PWM_MODE_MS)
wpi.pwmSetClock(384)	#19.2MHz / 384 = 50000Hz = 50KHz(0.02ms)
wpi.pwmSetRange(1000) # 0.02ms * 1000 = 20ms, 50KHz / 1000 = 50Hz

while True:
	answer = input("1:-90, 2:0, 3:+90, 4:quit > ")
	if answer =='1':
		#wpi.pwmWrite(PIN_SERVO, 25)	# 25 * 0.02ms = 0.5ms
		wpi.pwmWrite(PIN_SERVO, 50)	# 50 * 0.02ms = 1ms
	elif answer == '2':
		wpi.pwmWrite(PIN_SERVO, 75)	# 75 * 0.02ms = 1.5ms
	elif answer == '3':
		#wpi.pwmWrite(PIN_SERVO, 125)	# 125 * 0.02ms = 2.5ms 
		wpi.pwmWrite(PIN_SERVO, 100)	# 100 * 0.02ms = 2ms 
	elif answer == '9':
		break
