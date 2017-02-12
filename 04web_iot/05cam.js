var express = require('express');
var cv = require('opencv');
var app = express();


var camera = new cv.VideoCapture(0);
camera.setWidth(320);
camera.setHeight(240);

app.use(express.static(__dirname + '/static'));
app.get('/', function(req, res){
	res.redirect('/cam.html');
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


app.listen(5000, function(){
	console.log('server running on 5000.');
});