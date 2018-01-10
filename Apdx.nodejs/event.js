var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);
var wpi = require('wiringpi-node');

wpi.setup('wpi');

var pin = 25;
wpi.pinMode(pin, wpi.OUTPUT);

// unicast.html로 라우팅 설정
app.get ('/', function(req, res){
	res.sendFile(__dirname + '/event.html');
});

// 서버 실행, http://IP주소:8080
server.listen(8080, function(){
	console.log('server is running');
});

io.on('connection', function(socket){
  console.log('connection success!!');

	socket.on('ledon', function(){
	  console.log('led on!');
		wpi.digitalWrite(pin, wpi.HIGH);
	});

	socket.on('ledoff', function(){
	  console.log('led off!');
		wpi.digitalWrite(pin, wpi.LOW);
	});

});
