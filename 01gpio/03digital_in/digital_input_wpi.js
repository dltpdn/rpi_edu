const wpi = require('node-wiring-pi');
const PIN_BTN = 23;

wpi.wiringPiSetupGpio();
wpi.pinMode(PIN_BTN, wpi.INPUT);

let [val, old] = [-1,-1];
while(true){
	val = wpi.digitalRead(PIN_BTN);
	if(val != old){
		old = val;
		console.log(val);	
	}
}