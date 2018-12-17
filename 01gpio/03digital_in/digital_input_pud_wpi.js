const wpi = require('node-wiring-pi');

const PIN_BTN = 23;
let [val, old] = [-1, -1];

wpi.wiringPiSetupGpio();
wpi.pinMode(PIN_BTN, wpi.INPUT);
wpi.pullUpDnControl(PIN_BTN, wpi.PUD_DOWN);

while(true){
	val = wpi.digitalRead(PIN_BTN);
	if(val != old){
		old = val;
		console.log(val);
	}
}