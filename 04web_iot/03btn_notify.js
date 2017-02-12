var http = require('http');
var express = require('express');
var socketio = require('socket.io');
var onoff = require('onoff');

var app = express();
var server = http.createServer(app);
var io = socketio(server);
var sw_pin = new onoff.Gpio(23, 'in', 'both');

sw_pin.watch(function(err, value){
	console.log('btn: '+ value);
	io.emit('message', {data: value});
});

app.use(express.static(__dirname + '/static'));
app.get('/', function(req, res){
	res.redirect('/btn_notify.html');
});

io.on('connection', function(socket){
	console.log('connected' + socket.id);
	 socket.emit('message',{'data': 'welcome'});
});

server.listen(5000, function(){
	console.log('server running on 5000.');
});