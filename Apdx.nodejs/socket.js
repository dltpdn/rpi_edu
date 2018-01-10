var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(8080, function(){
        console.log('server is running');
});

// 경로 바인딩
app.get('/', function(req, res){
        res.sendFile(__dirname+ '/socket.html');
});

//socket 연결 이벤트 발생
io.on('connection', function(){
        console.log('connection');
});
