var wpi = require('wiring-pi');
var pin = 18;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.PWM_OUTPUT);
while(true){
	for(var i=0; i<=1024; i++){
		wpi.pwmWrite(pin, i);
		wpi.delay(1);
	}
	for(var i=1024; i>=0; i--){
		wpi.pwmWrite(pin, i);
		wpi.delay(1);
	}
			
}
