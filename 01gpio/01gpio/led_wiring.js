//npm install node-wiring-pi
var wpi = require('node-wiring-pi'); 
//var wpi = require('wiring-pi'); //install fail

wpi.wiringPiSetupGpio();
wpi.pinMode(18, wpi.OUTPUT);

for(var i=0; i<10; i++){
	wpi.digitalWrite(18, wpi.HIGH);
	console.log("LED On");
	wpi.delay(500);
	wpi.digitalWrite(18, wpi.LOW);
	console.log("LED Off");
	wpi.delay(500);
}