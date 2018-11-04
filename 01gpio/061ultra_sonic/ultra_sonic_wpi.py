import wiringpi as wpi, time
PIN_TRIG = 18
PIN_ECHO = 23

wpi.wiringPiSetupGpio();
wpi.pinMode(PIN_TRIG, wpi.OUTPUT);
wpi.pinMode(PIN_ECHO, wpi.INPUT);

while True:
	wpi.digitalWrite(PIN_TRIG, wpi.LOW)
	wpi.delay(200);
	wpi.digitalWrite(PIN_TRIG, wpi.HIGH)
	wpi.delayMicroseconds(10)
	wpi.digitalWrite(PIN_TRIG, wpi.LOW)
	while wpi.digitalRead(PIN_ECHO) == 0:
		start_time = time.time()
	while wpi.digitalRead(PIN_ECHO) == 1:
		end_time = time.time()
	travel_time = end_time - start_time
	distance = travel_time * 17160;
	print('Distance: %dCm '%round(distance, 2)  , travel_time)
