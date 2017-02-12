var onoff = require('onoff');
var led = new onoff.Gpio(18, 'out');

var sw = 1;
var cnt = 0;
var timer = setInterval(function(){
	led.writeSync(Number(sw));
	console.log(sw?'on':'off');
	sw = !sw;
	if(cnt++ > 10){
		clearInterval(timer);
	}
}, 500);  


process.on('SIGINT', function () {
	 led.unexport();
	 console.log('cleaned up.')
});