var express = require('express');
var app = express();
var onoff =require('onoff');
var pin_led = new onoff.Gpio(18, 'out');

app.use(express.static(__dirname + '/static'));
app.get('/', function(req, res){
	res.redirect('/led.html');
});

app.get('/operate/led', function(req, res){
	console.log(req.url, req.query);
	var val = req.param('val');
	if(val == 'on'){
		pin_led.writeSync(1);
		res.send('OK');
	}else if(val ==='off'){
		pin_led.writeSync(0);
		res.send('OK');
	}else{
		res.send('Fail');
	}
});


app.listen(5000, function(){
	console.log('server running on 5000.');
});