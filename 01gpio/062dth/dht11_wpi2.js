const wpi = require("node-wiringpi-js");

const PIN_DHT11 = 18;

let data  = []
let data2 = []
let cnt = 0

wpi.wiringPiSetupGpio();

while True:
	data  = [];
	data2 = [];
	cnt = 0;

	wpi.pinMode(PIN_DHT11, wpi.OUTPUT);
	wpi.digitalWrite(PIN_DHT11, wpi.HIGH);
	wpi.digitalWrite(PIN_DHT11, wpi.LOW);
	wpi.delay(18);
	wpi.digitalWrite(PIN_DHT11, wpi.HIGH);
	
	wpi.pinMode(PIN_DHT11, wpi.INPUT)
	wpi.pullUpDnControl(PIN_DHT11, wpi.PUD_UP)