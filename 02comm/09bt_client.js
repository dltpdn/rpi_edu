var btSerial = new (require('bluetooth-serial-port')).BluetoothSerialPort();
var address = "B8:27:EB:AD:74:74";
var channel = 3;

btSerial.connect(address, channel, function() {
	console.log('connected');
	var msg = new Buffer('Hello Bluetooth!!', 'utf-8');
	btSerial.write(msg, function(err, bytesWritten) {
		if (err) console.log(err);
	});

	btSerial.on('data', function(buffer) {
		console.log(buffer.toString('utf-8'));
	});
}, function() {
	console.log('cannot connect');
});
