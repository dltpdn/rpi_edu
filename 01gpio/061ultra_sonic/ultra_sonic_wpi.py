import wiringpi as wpi, time
pin_trig = 18
pin_echo = 23

wpi.wiringPiSetupGpio();
wpi.pinMode(pin_trig, wpi.OUTPUT);
wpi.pinMode(pin_echo, wpi.INPUT);

while True:
	wpi.digitalWrite(pin_trig, wpi.LOW)
	wpi.delay(200);
	wpi.digitalWrite(pin_trig, wpi.HIGH)
	wpi.delayMicroseconds(10)
	wpi.digitalWrite(pin_trig, wpi.LOW)
	while wpi.digitalRead(pin_echo) == 0:
		start_time = time.time()
	while wpi.digitalRead(pin_echo) == 1:
		end_time = time.time()
	travel_time = end_time - start_time
	distance = travel_time * 17160;
	print 'Distance: %dCm '%round(distance, 2)  , travel_time
