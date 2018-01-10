var oled = require('oled-spi');
var exec = require('child_process').exec;
var font = require('oled-font-5x7');
var pngparse = require('pngparse');

var opts = {
   width : 128,
   height : 64,
   dcPin : 23,
   rstPin : 24
};

var oled = new oled(opts);
oled.begin(function(){
	oled.clearDisplay();
	
	pngparse.parseFile('./lear.png', function(err, image){
		oled.drawBitmap(image.data);
		
		oled.setCursor(100,100);
		oled.writeString(font, 1, 'hello', 1, true);
	});	

});
