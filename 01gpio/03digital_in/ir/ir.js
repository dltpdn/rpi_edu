var onoff = require('onoff');
var pin = new onoff.Gpio(18, 'in', 'both');
var val = -1;
while(true){
	var read = pin.readSync();
	if(read != val){
		val = read;
		console.log(val == 0 ? 'no IR': 'IR detected');
	}
}

