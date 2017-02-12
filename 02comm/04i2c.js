var i2c = require('i2c');
var address = 0x04
var wire = new i2c(address, {device: '/dev/i2c-1'});

process.stdout.write("0=Led Off, 1=Led On, 3=Get Count > ");
process.stdin.on('data', function(data){
	data = Number(data.toString());
    if (data < 2){
        wire.writeByte(data, function(err){
        	if(err) console.log('write err:' + err.message);
        	else console.log( "Led ", data);
        });
    }else{
        wire.readByte(function(err, data){
        	console.log("Arduino LED Count", data);
        });
    }
});
    
