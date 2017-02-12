var wpi = require('wiring-pi');
var sw_pin = 18;

wpi.wiringPiSetupGpio();
wpi.pinMode(18, wpi.INPUT);

while(true){
	console.log(wpi.digitalRead(sw_pin));
}