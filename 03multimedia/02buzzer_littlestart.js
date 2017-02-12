var wpi = require('wiring-pi');
var sleep = require('sleep');

var pin = 18
var frequencies = {'c' : 262, 'd':294,'e':330,'f':349,'g':392,'a':440,'b':494};
var notes = 'ccggaag ffeeddc ggffeed ggffeed ccggaag ffeeddc'

wpi.wiringPiSetupGpio()

wpi.softToneCreate(pin)
for ( var i=0; i<notes.length; i++) {
	var note = notes[i];
	if (note != ' ')
		wpi.softToneWrite(pin, frequencies[note])
	else
		wpi.softToneWrite(pin, 0)
	sleep.msleep(300);
}

process.on('exit', function() {
	wpi.pinMode(pin, 0)
});
