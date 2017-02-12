const Raspi = require('raspi-io');
const five = require('johnny-five');
const board = new five.Board({
  io: new Raspi()
});

board.on('ready', function(){

  var led = new five.Led('GPIO18')
  led.blink(500);

});