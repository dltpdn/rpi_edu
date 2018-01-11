var wpi = require('wiringpi-node');
var readline = require('readline');

var rl = readline.createInterface(process.stdin, process.stdout); 
var pin = 18;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.PWM_OUTPUT);
wpi.pwmSetMode(wpi.PWM_MODE_MS);
wpi.pwmSetClock(192);
wpi.pwmSetRange(2000); //19.2M / 192 / 2000 = 50Hz, 1pwm = 0.01ms

rl.setPrompt("1:-90, 2:0, 3: +90 > ");

rl.prompt();
rl.on('line', function(answer){
	if(answer ==='1')	wpi.pwmWrite(pin, 50); // 50*0.01ms = 0.5ms 
	else if(answer === '2') wpi.pwmWrite(pin,150);
	else wpi.pwmWrite(pin, 250);
	rl.prompt();
}); 