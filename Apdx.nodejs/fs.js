var fs = require('fs');

console.log('START');

fs.writeFileSync('hello.txt', 'hello');
console.log('write old');


fs.writeFile('hello1.txt', 'hello', function(err){
	if(err){
		throw err;
	}

	console.log('write new');
});

console.log('END');
