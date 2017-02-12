var wpi = require('wiring-pi');
var pin = 18;

wpi.wiringPiSetupGpio();//wpi.setup('gpio');
wpi.pinMode(pin, wpi.INPUT);


var lastVal = -1;
while(true){
	var val = wpi.digitalRead(pin);
	if(val != lastVal){
		console.log(val ==0 ? 'dark' : 'light');
		lastVal = val;
	}
}
//wpi.wiringPiISR(pin, wpi.INT_EDGE_BOTH, function(){
//	var val = wpi.digitalRead(pin);
//});