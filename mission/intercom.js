var express = require('express');
var cv = require('opencv');
var wpi = require('wiring-pi');

var app = express();
var pin_servo = 18;
wpi.wiringPiSetupGpio();
wpi.pinMode(pin_servo, wpi.PWM_OUTPUT);
wpi.pwmSetMode(wpi.PWM_MODE_MS);
wpi.pwmSetClock(1920);
wpi.pwmSetRange(100);


var camera = new cv.VideoCapture(0);
camera.setWidth(320);
camera.setHeight(240);

app.use(express.static(__dirname + '/static'));
app.get('/', function(req, res){
	res.redirect('/intercom.html');
});

app.get('/cctv', function(req, res){
	console.log(req.url, req.query);
    camera.read(function(err, im) {
        if (err) throw err;
        else{
        	var buff = im.toBuffer();
        	var b64 = buff.toString('base64');
        	console.log(buff.length);
        	res.send(b64);
        }
      });	
});
app.get('/servo', function(req, res){
	console.log('servo ~~~~~~~~~');
	var val = req.param('val');
	wpi.pwmWrite(pin_servo,15);
	setTimeout(function(){
		wpi.pwmWrite(pin_servo,5);
	}, 1000);
	res.send('OK');
});

app.listen(5000, function(){
	console.log('server running on 5000.');
});