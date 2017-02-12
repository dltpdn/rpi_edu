var onoff = require('onoff');
var sw_pin = new onoff.Gpio(18, 'in', 'both');

//while(true){
//	console.log(sw_pin.readSync());
//}

sw_pin.read(function(err, value){
	console.log(value)
	sw_pin.read(arguments.callee);
});
