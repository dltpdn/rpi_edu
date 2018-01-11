var wpi = require('wiringpi-node');
var oled = require('oled-spi');
var font = require('oled-font-5x7');
var pngparse = require('pngparse');
var dht = require('node-dht-sensor');
var sleep = require('sleep');
var microtime = require('microtime');

var LED = 23; 
var PWM_LED = 24; 
var TRIG = 15;
var ECHO = 16;

wpi.setup('wpi');
wpi.pinMode(TRIG, wpi.OUTPUT);
wpi.pinMode(ECHO, wpi.INPUT);
wpi.pinMode(LED, wpi.OUTPUT);
wpi.digitalWrite(LED, wpi.LOW);
wpi.pinMode(PWM_LED, wpi.OUTPUT);
wpi.softPwmCreate(PWM_LED, 0, 100);

dht.initialize(11, 21);

var opts = {
	width:128,
	height:64,
	dcPin:23,
	rstPin:24
};

var oled = new oled(opts);

function pulseIn(pin, state){
	var MAX_LOOPS = 1000000;
	var numloops = 0;

	while(wpi.digitalRead(pin) != state){
		if(numloops++ == MAX_LOOPS)
			return 0;
	}

	var timeStart = microtime.now();

	while(wpi.digitalRead(pin) == state){
		if(numloops++ == MAX_LOOPS)
			return 0;
	}

	return microtime.now() - timeStart;
}

oled.begin(function(){
	oled.clearDisplay();
});

// Web-Server
var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

app.get ('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

server.listen(8080, function(){
	console.log('server is running');
});

io.on('connection', function(socket){
	console.log('connection');
	
	socket.on('setLed', function(data){
		console.log(data);
		wpi.digitalWrite(LED, Number(data));	
	});
	
	socket.on('setRangeLed', function(data){
		console.log(data);
		wpi.softPwmWrite(PWM_LED, Number(data));
	});
	
	socket.on('setText', function(data){
		console.log(data);
		oled.clearDisplay();
		oled.setCursor(1,1);
		oled.writeString(font, 2, data.toString(), 1, true);
	});

	socket.on('disconnect', function(){
		console.log('disconnect');
	});
});

setInterval(function(){
	// distance
	wpi.digitalWrite(TRIG, wpi.LOW);
	sleep.usleep(2);	
	wpi.digitalWrite(TRIG, wpi.HIGH);
	sleep.usleep(20);
	wpi.digitalWrite(TRIG, wpi.LOW);
	var duration = pulseIn(ECHO, wpi.HIGH);
	var distance = Math.floor(duration / 58); // cm
	
	// temperature & humidity
	var data = dht.read();
	var temperature = Math.floor(data.temperature);
	var humidity = Math.floor(data.humidity);

	io.emit('info', {distance:distance, temperature:temperature, humidity:humidity});
}, 3000);

