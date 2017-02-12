var onoff =require('onoff');
var readline = require('readline');
var rl = readline.createInterface(process.stdin, process.stdout);
var pin_led = new onoff.Gpio(18, 'out');


rl.setPrompt("1:On, 0:Off >");

rl.prompt();
rl.on('line', function(answer){
	pin_led.writeSync(Number(answer));
	rl.prompt();
});