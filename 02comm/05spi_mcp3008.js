var SPI = require('pi-spi');
var spi = SPI.initialize("/dev/spidev0.0");
spi.clockSpeed(10000);

function analog_read(channel){
	var req = Buffer.from([1, (8 + channel)<<4, 0]);
	spi.transfer(req, req.length, function(err, res){
		if(err){
			console.log(err.message);
		}else{
			console.log(res.toString('hex'));
			var result = (((res[1] &3) << 8) + res[2]);
			console.log(result, (result * 3.3 / 1024).toFixed(1) +'v');
		}
	});
}
setInterval(function(){
	analog_read(0);
}, 500);
