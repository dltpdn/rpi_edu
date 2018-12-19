var wpi = require('node-wiring-pi');
let fd = wpi.wiringPiSPISetup (0, 10000);

function analog_read(channel){
	var data = Buffer.from([1, (8 + channel)<<4, 0]);
	wpi.wiringPiSPIDataRW(0, data)
	console.log(data.toString('hex'));
	var result = (((data[1] &3) << 8) + data[2]);
	console.log(result, (result * 3.3 / 1024).toFixed(1) +'v');
}
setInterval(function(){
	analog_read(0);
}, 500);
