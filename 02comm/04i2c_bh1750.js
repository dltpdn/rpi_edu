var bh1750 = require('bh1750');
var light = new bh1750({
        address:0x23,
        device:'/dev/i2c-1',
        command:0x10,
        length : 2
});

setInterval(function(){
        light.readLight(function(value){
                console.log(value + 'lux');
        });
}, 1000);