var rsj = require('rsj');

rsj.r2j('http://fs.jtbc.joins.com/RSS/newsflash.xml', function(json){
	var data = JSON.parse(json);

	for(var i = 0; i < 10; i++){
		console.log(data[i].title);
	}
});
