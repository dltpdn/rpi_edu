var player = require('play-sound');
var audio = null;

process.stdout.write('0: stop, 1:play>');
process.stdin.on('data', function(data){
	if(data.toString().trim() === '1'){
		// $ mplayer foo.mp3  
		audio = player.play('sample.mp3', function(err){
		  if (err) throw err
		})
	}else{
		if(audio){
			audio.kill();
		}
	}
	process.stdout.write('0: stop, 1:play>');
});
 