var http = require('http');
var express = require('express');
var socketio = require('socket.io');
var onoff =require('onoff');
var sensor = require('node-dht-sensor');

var app = express();
var server = http.createServer(app);
var io = socketio(server);

var pin_led = new onoff.Gpio(18, 'out');
var sw_pin = new onoff.Gpio(23, 'in', 'both');
var dht_type = 11;
var pin_dht = 24

sw_pin.watch(function(err, value){
	console.log('btn: '+ value);
	io.emit('message', {data: value});
});


app.use(express.static(__dirname + '/static'));
app.get('/', function(req, res){
	res.redirect('/web_iot.html');
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

app.get('/monitor', function(req, res){
	console.log(req.url, req.query);
	sensor.read(dht_type, pin_dht, function(err, temperature, humidity){
		if(!err){
			var obj = {'humi' : humidity, 'temp' : temperature};
		}else{
			var obj = {'humi' : 'err', 'temp' : 'err'};
		}
		console.log(JSON.stringify(obj));
		res.send(obj);
	});
});

io.on('connection', function(socket){
	console.log('connected' + socket.id);
	 socket.emit('message',{'data': 'welcome'});
});

server.listen(5000, function(){
	console.log('server running on 5000.');
});