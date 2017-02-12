var btSerial = new (require('bluetooth-serial-port')).BluetoothSerialPort();
 
btSerial.on('found', function(address, name) {
    console.log(address, name);
});
 
btSerial.inquire();