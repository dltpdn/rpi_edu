var exec = require('child_process').exec;

exec('./hello', function(err, stdout){
	console.log(stdout);
});
