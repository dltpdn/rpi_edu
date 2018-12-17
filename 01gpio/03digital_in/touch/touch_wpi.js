var wpi = require('node-wiring-pi');
var pin = 23;

wpi.wiringPiSetupGpio();//wpi.setup('gpio');
wpi.pinMode(pin, wpi.INPUT);

while(true){
	var read = wpi.digitalRead(pin);
	if(read){
		console.log("touch");
	}
}