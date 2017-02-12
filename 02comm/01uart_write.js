var SerialPort = require('serialport');
var port = new SerialPort("/dev/ttyS0", {baudRate:115200}, function(err){
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