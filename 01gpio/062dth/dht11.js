var sensor = require('node-dht-sensor');
var dht = 11;
var pin = 18;

function dht_cb(err, temperature, humidity) {
    if (!err) {
        console.log('temp: ' + temperature.toFixed(1) + '°C, ' +
            'humidity: ' + humidity.toFixed(1) + '%'
        );
    }else{
    	console.log(err);
    }
    setTimeout(function(){
    	sensor.read(dht, pin, dht_cb);
    }, 100);
    
}
sensor.read(dht, pin, dht_cb);

