var wpi = require('wiring-pi');

var pin = 18;
wpi.wiringPiSetupGpio();
wpi.pinMode(pin, wpi.INPUT);
wpi.pullUpDnControl(pin, wpi.PUD_DOWN);

while(true){
	console.log(wpi.digitalRead(pin));
}