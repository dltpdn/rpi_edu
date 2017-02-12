var onoff = require('onoff');
var sw_pin = new onoff.Gpio(18, 'in', 'both');


sw_pin.watch(function(err, value){
	console.log(value);
});