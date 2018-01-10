var exec = require('child_process').exec;
var spawn = require('child_process').spawn;

/*
exec('mplayer test.mp3', function(err, stdout){
	if(err){
		console.log('err :' + err);
	}
	console.log('stdout : ' + stdout);
});
*/
var sp = spawn('mplayer', ['test.mp3']);

sp.on('exit', function(){
	console.log('exit');
});

sp.stdout.on('data', function(data){
	console.log('stdout : ' + data);
});

sp.stderr.on('data', function(data){
	console.log('stderr : ' + data);
});
