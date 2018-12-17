var wpi = require('node-wiring-pi');
var readline = require('readline');

var rl = readline.createInterface(process.stdin, process.stdout); 
var pin = 18;

wpi.setup('gpio');
wpi.pinMode(pin, wpi.PWM_OUTPUT);
wpi.pwmSetMode(wpi.PWM_MODE_MS);
wpi.pwmSetClock(1920);
wpi.pwmSetRange(200); //19.2M / 1920 / 200 = 50Hz, 1pulse = 0.1ms

rl.setPrompt("1:-90, 2:0, 3: +90 > ");

rl.prompt();
rl.on('line', function(answer){
	if(answer ==='1')	wpi.pwmWrite(pin, 5); // 5*0.1ms = 0.5ms 
	else if(answer === '2') wpi.pwmWrite(pin,15); //15 * 0.1ms = 1.5ms
	else wpi.pwmWrite(pin, 25);					// 25 * 0.1ms = 2.5ms
	rl.prompt();
}); 