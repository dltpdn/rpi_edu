var wpi = require('wiring-pi');
var sleep = require('sleep');

var pin = 18

wpi.wiringPiSetupGpio()
wpi.softToneCreate(pin)
while (true) {
	wpi.softToneWrite(pin, 392)
	sleep.msleep(500);
	wpi.softToneWrite(pin, 523)
	sleep.msleep(500);
}

process.on('exit', function() {
	wpi.softToneWrite(pin, 0);
});
