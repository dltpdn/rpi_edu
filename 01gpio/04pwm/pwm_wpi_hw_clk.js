var wpi = require('wiring-pi');
var pin = 18;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.PWM_OUTPUT);
wpi.pwmSetClock(1920);
wpi.pwmSetRange(1000);

while(true){
	for(var i=0; i<=1000; i++){
		wpi.pwmWrite(pin, i);
		wpi.delay(1);
	}
	for(var i=1000; i>=0; i--){
		wpi.pwmWrite(pin, i);
		wpi.delay(1);
	}
			
}
