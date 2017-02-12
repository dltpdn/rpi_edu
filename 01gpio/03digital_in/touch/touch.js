var onoff = require('onoff');
var pin = new onoff.Gpio(18, 'in', 'both');

while(true){
	var read = pin.readSync();
	if(read){
		console.log('touched');
	}
}

