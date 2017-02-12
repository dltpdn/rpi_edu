var wpi = require('wiring-pi');
var pin = 18;

wpi.wiringPiSetupGpio();//wpi.setup('gpio');
wpi.pinMode(pin, wpi.INPUT);

var val = -1;
while(true){
	var read = wpi.digitalRead(pin);
	if(read != val){
		val = read;
		console.log(val == 0 ? "no intruder" : "intruder detected");
	}
}