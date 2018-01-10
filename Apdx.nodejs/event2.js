
var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

// unicast.html로 라우팅 설정
app.get ('/', function(req, res){
	res.sendFile(__dirname + '/event2.html');
});

// 서버 실행, http://IP주소:8080
server.listen(8080, function(){
	console.log('server is running');
});

io.on('connection', function(socket){
  console.log('connection success!!');

  var i = 0;
  setInterval(function(){
    socket.emit('msg', i);
    i++;
	}, 1000);
});
