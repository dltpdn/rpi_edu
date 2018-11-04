import wiringpi as wpi
PIN_CHARGE = 18
PIN_MEASURE = 23

wpi.wiringSetupGpio();
while True:
	wpi.pinMode(PIN_CHARGE, wpi.INPUT)
	wpi.pinMode(PIN_MEASURE, wpi.OUTPUT)
	wpi.digitalWrite(PIN_MEASURE, wpi.LOW)
	wpi.delay(100)
	
	wpi.pinMode(PIN_CHARGE, wpi.OUTPUT)
	wpi.pinMode(PIN_MEASURE, wpi.INPUT)
	wpi.digitalWrite(PIN_CHARGE, wpi.HIGH)
	count = 0
	
	while not(wpi.digitalRead(PIN_MEASURE)) :
		count+=1
	print(count)
