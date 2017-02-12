var wpi = require('wiring-pi');
var pin_charge = 18;
var pin_measure = 23;

wpi.wiringSetupGpio();
while(true){
	wpi.pinMode(pin_charge, wpi.INPUT);
	wpi.pinMode(pin_measure, wpi.OUTPUT);
	wpi.digitalWrite(pin_measure, wpi.LOW);
	wpi.delay(100);
	wpi.pinMode(pin_charge, wpi.OUTPUT);
	wpi.pinMode(pin_measure, wpi.INPUT);
	wpi.digitalWrite(pin_charge, wpi.HIGH);
	var count = 0;
	while(!wpi.digitalRead(pin_measure) ){
		count++;
	}
	console.log(count);
}