var SerialPort = require('serialport');
var port = new SerialPort("/dev/serial0", {baudRate:9600}, function(err){
	if(err){
		console.log('err:' + err.message);
	}else{
		var line = '';
		port.on('data', function(data){
			if(data =='\r'){
				console.log('recv:' + line +'\r');	
				line = '';
			}else{
				line +=data;
			}
			
		});
	}
});
