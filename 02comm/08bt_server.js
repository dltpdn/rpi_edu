var server = new(require('bluetooth-serial-port')).BluetoothSerialPortServer();
 
var PORT = 3;
 
server.listen(function (clientAddress) {
    console.log('Client: ' + clientAddress + ' connected!');
    server.on('data', function(buffer) {
        console.log('Received data from client: ' + buffer);
 
        console.log('Sending data to the client');
        server.write(new Buffer('Good Bye!'), function (err, bytesWritten) {
            if (err) {
                console.log('Error!');
            } else {
                console.log('Send ' + bytesWritten + ' to the client!');
            }
        });
    });
}, function(error){
    console.error("Something wrong happened!:" + error);
}, { channel: PORT} );