var wpi = require('wiring-pi');
var pin_trig = 18;
var pin_echo = 23;
var start_time = end_time = travel_time =  distance = 0;

wpi.wiringPiSetupGpio();
wpi.pinMode(pin_trig, wpi.OUTPUT);
wpi.pinMode(pin_echo, wpi.INPUT);

while(true){
	wpi.digitalWrite(pin_trig, wpi.LOW);
	wpi.delay(200);
	wpi.digitalWrite(pin_trig, wpi.HIGH);
	wpi.delayMicroseconds(10);
	wpi.digitalWrite(pin_trig, wpi.LOW);
	while(wpi.digitalRead(pin_echo) === 0){
		start_time = process.hrtime();
	}
	while(wpi.digitalRead(pin_echo) === 1){
		end_time = process.hrtime(start_time);
	}
	travel_time = end_time[0] + (end_time[1] * 1e-9);
	distance = travel_time * 17160;
	console.log(distance.toFixed(2) + 'cm ' + travel_time);
}