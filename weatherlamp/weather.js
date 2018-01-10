var Forecast = require('forecast');
var wpi = require('wiringpi-node');
var oled = require('oled-spi');
var font = require('oled-font-5x7');
var pngparse = require('pngparse');

wpi.setup('wpi');

var icon_path = "./image/";
var pin1 = 8;
var pin2 = 9;
var pin3 = 7;

wpi.pinMode(pin1, wpi.OUTPUT);
wpi.pinMode(pin2, wpi.OUTPUT);
wpi.pinMode(pin3, wpi.OUTPUT);

wpi.digitalWrite(pin1, wpi.LOW);
wpi.digitalWrite(pin2, wpi.LOW);
wpi.digitalWrite(pin3, wpi.LOW);


var opts = {
	widht:128,
	height: 64,
	dcPin: 23,
	rstPin: 24
};

var forecast = new Forecast({
	service: 'darksky',
	key: 'c2078eb9649112e9ac18ed7d6f1905e9',
	units: 'celcius',
	cache: true,
	ttl: {
	minutes: 27,
	seconds: 45
	}
});

var oled = new oled(opts);
var weatherTime = 'cloudy';
var temperature = '100';
var weatherIcon = 'cloud.png';

var decode_weather = function(weatherTime){
	var textWeather = ['clear', 'rain', 'snow', 'sleet', 'wind', 'fog', 'cloudy'];

	for(var i = 0; i < textWeather.length; i++)
	{
		if(weatherTime.indexOf(textWeather[i]) > -1)
		{
			if(textWeather[i] == 'clear')
			{
				wpi.digitalWrite(pin1, wpi.HIGH);
				wpi.digitalWrite(pin2, wpi.LOW);
				wpi.digitalWrite(pin3, wpi.LOW);
			}
			else if(textWeather[i] == 'fog' || textWeather[i] == 'cloudy' || textWeather[i] == 'wind')
			{
				wpi.digitalWrite(pin1, wpi.LOW);
				wpi.digitalWrite(pin2, wpi.HIGH);
				wpi.digitalWrite(pin3, wpi.LOW);
			}
			else
			{
				wpi.digitalWrite(pin1, wpi.LOW);
				wpi.digitalWrite(pin2, wpi.LOW);
				wpi.digitalWrite(pin3, wpi.HIGH);
			}	
			return textWeather[i];
		}
	}
	return 'ERROR';
};

var icon_weather = function(weatherTime){
	if(weatherTime == 'clear')
		return 'clear.png';
	if(weatherTime == 'cloudy')
		return 'cloud.png';
	if(weatherTime == 'rain')
		return 'rain.png';
	if(weatherTime == 'snow')
		return 'snow.png';
	if(weatherTime == 'sleet')
		return 'sleet.png';
	if(weatherTime == 'wind')
		return 'wind.png';
	if(weatherTime == 'fog')
		return 'fog.png';
}; 

function updateWeather(){
	forecast.get([37.566535, 126.97796919999996], function(err, weather){
		if(weather)
		{
			console.log(weather.currently.icon);
			weatherTime = decode_weather(weather.currently.icon);
			temperature = parseInt(Math.ceil(weather.currently.temperature)) + 'c\'';
			weatherIcon = icon_weather(weatherTime);
		
			pngparse.parseFile(icon_path + weatherIcon, function(err, image){
				oled.drawBitmap(image.data);
				oled.setCursor(65,3);
				oled.writeString(font, 1, weatherTime, 1, true);
				oled.setCursor(70, 30);
				oled.writeString(font, 2, String(temperature), 1, true);
			});
		}
		else
		{
		updateWeather();
		}
	});
};

oled.begin(function(){
	oled.clearDisplay();

	updateWeather();

	setInterval(function(){
		var date = new Date();

		if((date.getMinutes() == 0) && (date.getSeconds() == 0))
		{
			oled.clearDisplay();
			
			updateWeather();
		}
	}, 1000);
});
