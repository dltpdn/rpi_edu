var wpi = require('wiring-pi');
var pin = 18;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.OUTPUT);
wpi.softPwmCreate(pin, 0, 100);

while(true){
	for(var i=0; i<=100; i++){
		wpi.softPwmWrite(pin, i);
		wpi.delay(10);
	}
	for(var i=100; i>=0; i--){
		wpi.softPwmWrite(pin, i);
		wpi.delay(10);
	}
			
}
