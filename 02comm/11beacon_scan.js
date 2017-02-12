var noble = require('noble');
noble.state = "poweredOn";

noble.on('stateChange', function(state){
	console.log(state);
	if(state == "poweredOn"){
		noble.startScanning([], true, function(err){
			console.log('err:'+err);
		});
	}
});
noble.on('scanStart', function(){
	console.log('scanStart');
});
noble.on('scanStop', function(){
	console.log('scanStop');
});

noble.on('discover', function(peripheral) { 

  var macAddress = peripheral.uuid;
  var rss = peripheral.rssi;
  var localName = peripheral.advertisement.localName; 
  console.log('found device: ', macAddress, ' ', localName, ' ', rss);   
});