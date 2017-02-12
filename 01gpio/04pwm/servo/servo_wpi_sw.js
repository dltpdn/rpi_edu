var wpi = require('wiring-pi');
var readline = require('readline');

var rl = readline.createInterface(process.stdin, process.stdout); 
var pin = 18;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.OUTPUT);
wpi.softPwmCreate(pin, 5, 100);

rl.setPrompt("1:-90, 2:0, 3: +90 > ");

rl.prompt();
rl.on('line', function(answer){
	if(answer ==='1')	wpi.softPwmWrite(pin, 5);
	else if(answer === '2') wpi.softPwmWrite(pin,15);
	else wpi.softPwmWrite(pin, 25);
	rl.prompt();
});


