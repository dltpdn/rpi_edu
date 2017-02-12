var onoff = require('onoff');
var pin = new onoff.Gpio(18, 'in', 'both');

console.log(pin.readSync() == 0 ? 'dark': 'light');

pin.watch(function(err, value){
	console.log(value==0 ? 'dark' : 'light');
});
