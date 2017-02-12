#include <Wire.h>

#define ADDR 0x04
#define PIN_LED 13

int cnt = 0;
int lastVal = -1;

void setup() {
  Wire.begin(ADDR);
  Wire.onReceive(onRecv);
  Wire.onRequest(onReq);
  
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("ready.");
}

void loop() {
  delay(100);
}

void onRecv(int bytes){
  int val;
  while(Wire.available()){
    val = Wire.read();
    
    Serial.print("read:");
    Serial.println(val);
    if(lastVal != val){
      lastVal = val;
      cnt++;
      if(val == 1){
        digitalWrite(PIN_LED, HIGH);      
      }else if(val == 0){
        digitalWrite(PIN_LED, LOW);
      }
    }
  }
}

void onReq(){
  Serial.print("req:");
  Serial.println(cnt);
  Wire.write(cnt);
}
