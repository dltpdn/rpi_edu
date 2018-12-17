var wpi = require('node-wiring-pi'); //npm install node-wiring-pi
//var wpi = require('wiring-pi');
//var wpi = require('wiringpi-node');
console.log(wpi);

//wpi.setup('gpio');
wpi.wiringPiSetupGpio();
wpi.pinMode(18, wpi.OUTPUT);

var cnt = 0;
var sw = true;
//var timer = setInterval(function(){
//	if(sw){
//		wpi.digitalWrite(18, wpi.HIGH);
//	}else{
//		wpi.digitalWrite(18, wpi.LOW);
//	}
//	sw = !sw;
//	if(cnt++ > 10) clearInterval(timer);
//}, 500);

for(var i=0; i<10; i++){
	wpi.digitalWrite(18, wpi.HIGH);
	wpi.delay(500);
	wpi.digitalWrite(18, wpi.LOW);
	wpi.delay(500);
}