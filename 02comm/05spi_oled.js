var oled = require('oled-spi');
var exec= require('child_process').exec;
var font = require('oled-font-5x7');
var opts = {
        width : 128,
        height : 64,
        dcPin : 23,
        rstPin : 24
};

var oled = new oled(opts);
oled.begin(function(){
        oled.clearDisplay();
        setInterval(function(){
                exec('date +%H:%M:%S', function(err, stdout, stderr){
                        oled.setCursor(0,0);
                        oled.writeString(font, 2, stdout, 1, true);
                });
        }, 1000);
});
