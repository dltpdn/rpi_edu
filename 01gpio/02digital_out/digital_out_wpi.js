var wpi = require('wiring-pi');
var readline = require('readline');

var rl = readline.createInterface(process.stdin, process.stdout);

var pin = 18;
wpi.setup('gpio');
wpi.pinMode(pin, wpi.OUTPUT);

rl.setPrompt("1:On, 0:Off >");

rl.prompt();
rl.on('line', function(answer){
	wpi.digitalWrite(pin, Number(answer));
	rl.prompt();
});