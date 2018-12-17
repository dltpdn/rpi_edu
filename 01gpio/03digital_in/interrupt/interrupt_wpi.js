var wpi = require('node-wiring-pi');
var pin = 23;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.INPUT);

wpi.wiringPiISR(pin, wpi.INT_EDGE_BOTH, function(){
	console.log(wpi.digitalRead(pin));
});


