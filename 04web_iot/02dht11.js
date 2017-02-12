var express = require('express');
var app = express();
var sensor = require('node-dht-sensor');
var dht_type = 11;
var pin_dht = 24

app.use(express.static(__dirname + '/static'));
app.get('/', function(req, res){
	res.redirect('/dht11.html');
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


app.listen(5000, function(){
	console.log('server running on 5000.');
});