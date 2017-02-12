var onoff = require('onoff');

(function measure(){
	var count = 0;
	var pin_charge = new onoff.Gpio(18, 'in');
	var pin_measure = new onoff.Gpio(23, 'out');
	pin_measure.writeSync(0);
	setTimeout(function(){
		pin_charge.unexport();
		pin_measure.unexport();
		
		pin_charge = new onoff.Gpio(18, 'out');
		pin_measure = new onoff.Gpio(23, 'in');
		pin_charge.write(1, function(err){
			if(!err){
				while(pin_measure.readSync() === 0 ){
					count++;
				}
				console.log(count);
				pin_charge.unexport();
				pin_measure.unexport();
				measure();
			}
		});
	}, 10);
})();

