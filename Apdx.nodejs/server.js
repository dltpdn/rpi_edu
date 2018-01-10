var server = require('http').createServer(function(req, res){
	res.writeHead(200, {'Content-Type':'text/html'});
	res.end('<h1> hello world </h1>');
}).listen(8080, function(){
	console.log('server is running');
});
