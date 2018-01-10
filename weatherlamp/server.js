var Forecast = require('forecast');
var wpi = require('wiringpi-node');
var oled = require('oled-spi');
var font = require('oled-font-5x7');
var pngparse = require('pngparse');
var exec = require('child_process').exec;
var request = require('request');
var fs = require('fs');
var rsj = require('rsj');

var pin1 = 8;
var pin2 = 9;
var pin3 = 7;
var icon_path = "./image/";
wpi.setup('wpi');

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
var weatherType = '';
var temperature = 0;
var humidity = 0;
var weatherIcon = '';
var latitude;
var longitude;
var address = 'none';
var ip = 'none';
var news= [];
var status = true;

var decode_weather = function(data){
	var textWeather = ['clear', 'rain', 'snow', 'sleet', 'wind', 'fog', 'cloudy'];

	for(var i = 0; i < textWeather.length; i++)
	{
		if(data.indexOf(textWeather[i]) > -1)
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

var icon_weather = function(data){
	if(data == 'clear')
		return 'clear.png';
	if(data == 'cloudy')
		return 'cloud.png';
	if(data == 'rain')
		return 'rain.png';
	if(data == 'snow')
		return 'snow.png';
	if(data == 'sleet')
		return 'sleet.png';
	if(data == 'wind')
		return 'wind.png';
	if(data == 'fog')
		return 'fog.png';
}; 

// 정해진 위도 경도로 날씨, 온도 가져오기
function updateWeather(){
	forecast.get([latitude, longitude], function(err, weather){
		if(!err){
			if(weather){
				console.log(weather.currently.icon);
				weatherType = decode_weather(weather.currently.icon);
				temperature = parseInt(Math.ceil(weather.currently.temperature)) + '\'c';
				humidity = (weather.currently.humidity * 100) + '  %';				
				weatherIcon = icon_weather(weatherType);
			}
			else{
				setTimeout(function(){
					updateWeather();
				}, 100);
			}
		}
		else{
			console.log('update weather error');
		}
	});
};

// 저장된 위도, 경도로 주소 가져오기
function updateAddress(){
	var geocode = "http://maps.googleapis.com/maps/api/geocode/json?address=" + latitude + "," + longitude+ "&sensor=false&language=ko";
			    
	request(geocode, function (error, response, data) {
		address = 'none';
			        
		if (!error && response.statusCode == 200) {
			data = JSON.parse(data);
			if(data.status == 'OK') {
				address = data.results[0].formatted_address;
			}
		}
		else{
			console.log('update Address error');
		}
	});
};

// JTBC 뉴스 속보 중 10개 가져오기
function updateNews(){
	rsj.r2j('http://fs.jtbc.joins.com//RSS/newsflash.xml',function(json) {
		var data = JSON.parse(json);
		news=[];
			
		for(var i = 0; i < 10; i++) {
			news[i]= {title:data[i].title, link:data[i].link};
		}
	});	
};
/*
function checkWifi(){
	exec('if nc -zw1 google.com 80; then echo "on";fi', function(err, data){
		if(data.indexOf('on')>-1){
			if(status == false){
				updateWeather();
				updateNews();
			}
			status = true;
		}
		else {
			status = false;	
		}
	});
};

checkWifi();

setInterval(function(){
//	checkWifi();
}, 10000);
*/
oled.begin(function(){
	oled.clearDisplay();

	var tmp = fs.readFileSync(__dirname + '/location', 'utf8');
	latitude = tmp.split(',')[0];
	longitude = tmp.split(',')[1];
	
	if(status == true){
		updateAddress();
		updateWeather();
		updateNews();
	}
	
	oled.setCursor(1, 16);
	oled.writeString(font, 3, "Weather", 1, true);
		
	setTimeout(function(){
		setInterval(function(){
			var date = new Date();

			// 정각
			if(status == true && (date.getMinutes() == 0) && (date.getSeconds() == 0))
			{
				updateWeather();
				updateNews();	
			}
			
			// 5초에 한번 % 는 나누기 연산
			if(date.getSeconds() % 5 == 0){			
				io.emit('info', {news:news, address:address, weather:weatherType, temperature:temperature,  humidity:humidity, location:latitude + ',' + longitude});
			}
			
			// 10초에 한번 % 는 나누기 연산
			if(date.getSeconds() % 10 == 0){
				if(status == true){
					pngparse.parseFile(icon_path + weatherIcon, function(err, image){
						oled.clearDisplay();
						if(!err){
							oled.drawBitmap(image.data);
						}
				
						oled.setCursor(65, 3);
						oled.writeString(font, 1, weatherType, 1, true);
						oled.setCursor(70, 30);
						oled.writeString(font, 2, String(temperature), 1, true);

					});
				}
				else{
						oled.clearDisplay();
						oled.setCursor(1, 1);
						oled.writeString(font, 2, "Wifi", 1, true);
						oled.setCursor(1, 20);
						oled.writeString(font, 2, "Connect Error!!", 1, true);
				}
			}
			
			if(status == true && date.getSeconds() % 10 == 6){
				// ip 주소 가져오기
				exec('hostname -I', function(err, stdout){
					if(stdout.toString().indexOf('.') > -1){
						ip = stdout.split(' ')[0];
					}

					oled.clearDisplay();
					oled.setCursor(1, 1);
					oled.writeString(font, 2, 'infomation', 1, true);
					oled.setCursor(1, 20);
					oled.writeString(font, 3, date.getHours()+ ':'+(date.getMinutes()<10?'0':'')+date.getMinutes(), 1, true);
					oled.setCursor(1, 48);
					oled.writeString(font, 1, 'ip: ' + ip, 1, true);
				});
			}
		}, 1000);
	}, 1000);
});

// 웹서버 관련 소스
var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

// index.html로 라우팅 설정
app.get ('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

// 서버 구동, http://IP주소
server.listen(8080, function(){
	console.log('server is running');
});

// 클라이언트 접속 시, 이벤트 등록
io.on('connection', function(socket){
	console.log('connection');
	
	// index.html에서 change_location으로 메시지 오면 이벤트 발생
	socket.on('change_location', function(data){
		latitude = data.latitude;
		longitude = data.longitude;

		if(status == true){
			updateAddress();
			updateWeather();
			updateNews();
		}
		
		fs.writeFileSync(__dirname + '/location', latitude +','+longitude);
	});

	socket.on('disconnect', function(){
		console.log('disconnect');
	});
});
