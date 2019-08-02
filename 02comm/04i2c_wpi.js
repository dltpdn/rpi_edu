var wpi = require('node-wiring-pi');
var address = 0x04
var device = '/dev/i2c-1';
var fd = wpi.wiringPiI2CSetupInterface(device, address)

process.stdout.write("0=Led Off, 1=Led On, 3=Get Count > ");
process.stdin.on('data', function(data){
	data = Number(data.toString());
    if (data < 2){
    	wpi.wiringPiI2CWrite(fd, data)
        
    }else{
    	var val = wpi.wiringPiI2CRead(fd);
    	console.log(val);
       
    }
});
    
