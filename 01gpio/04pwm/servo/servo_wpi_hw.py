# run with sudo!!
import wiringpi as wpi
pin = 18

wpi.wiringPiSetupGpio()
wpi.pinMode(pin, wpi.PWM_OUTPUT)
wpi.pwmSetMode(wpi.PWM_MODE_MS)
wpi.pwmSetClock(384)	#19.2MHz / 384 = 50000Hz = 50KHz(0.02ms)
wpi.pwmSetRange(1000) # 0.02ms * 1000 = 20ms, 50KHz / 1000 = 50Hz

while True:
	answer = raw_input("1:-90, 2:0, 3: +90 > ")
	if answer =='1':
		wpi.pwmWrite(pin, 25)	# 25 * 0.02ms = 0.5ms
	elif answer == '2':
		wpi.pwmWrite(pin, 75)	# 75 * 0.02ms = 1.5ms
	else:
		wpi.pwmWrite(pin, 125)	# 125 * 0.02ms = 2.5ms 
