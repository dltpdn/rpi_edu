var dht = require('node-dht-sensor');

dht.initialize(11, 18);

setInterval(function(){

	var data = dht.read();
	var temp = data.temperature.toFixed(1);
	var humi = data.humidity.toFixed(1);
	
   console.log('Temeperature : '  + temp + 'C, Humidity : ' + humi + ' %') ;
}, 1000);
