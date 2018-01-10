var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

// unicast.html로 라우팅 설정
app.get ('/', function(req, res){
	res.sendFile(__dirname + '/unicast.html');
});

// 서버 실행, http://IP주소:8080
server.listen(8080, function(){
	console.log('server is running');
});

// USER1, USER2를 위한 소켓 생성
var sock_user1;
var sock_user2;

io.on('connection', function(socket){

	//USER에 대한 소켓 할당
	socket.on('user', function(data){
		if(data == 'user1')
			sock_user1 = socket;
		else if(data == 'user2')
			sock_user2 = socket;
	});

	 //USER1이면USER2에게, USER2이면 USER1에게 1:1 통신
	 socket.on('msg', function(data){
	 	console.log(data.me + ' : ' + data.msg);

		if(data.me == 'user1')
			sock_user2.emit('msg', data);
		else if(data.me == 'user2')
			sock_user1.emit('msg', data);
	 });
});
