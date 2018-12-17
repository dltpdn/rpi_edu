var SerialPort = require('serialport');
var port = new SerialPort("/dev/serial0", {baudRate:9600}, function(err){
	if(err){
		console.log('err:' + err.message);
		port = null;
	}
});
if(port){
	process.stdout.write('>');
	process.stdin.on('data', function(data){
		port.write(data+'\r');
		process.stdout.write('>');
	});
}