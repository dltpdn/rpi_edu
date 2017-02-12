var wpi = require('wiring-pi');
var pin = 18;

wpi.wiringPiSetupGpio();//wpi.setup('gpio');
wpi.pinMode(pin, wpi.INPUT);

while(true){
	var read = wpi.digitalRead(pin);
	if(read){
		console.log("touch");
	}
}