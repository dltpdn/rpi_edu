var LCD = require('lcdi2c'); //npm install lcdi2c
var lcd = new LCD( 1, 0x3f, 16, 2 );

lcd.clear();
lcd.println( 'Hello World!',1);
lcd.println( 'Hello Raspberry!',2);
//lcd.createChar( 0,[ 0x10,0x8,0x4,0x2,0x1,0x2,0x1c]); 
