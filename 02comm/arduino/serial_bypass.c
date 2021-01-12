/*
 아두이노와 라즈베리 파이의 UART 연결
 아두이노 : SoftSerial
 라즈베리파이 : GPIO UART
*/

#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX

void setup()
{
  Serial.begin(9600);
  Serial.println("Start UART test");  // PC의 시리얼 모니터에 표시합니다.
  mySerial.begin(9600); //소프트 시리얼로 라즈베리 파이와 통신하게 됩니다.
}

void loop() {
  // 라즈베리 파이에서 넘어온 데이터가 있으면 PC로 넘겨줍니다.
  if (mySerial.available())
    Serial.write(mySerial.read());
  // PC에서 넘어온 데이터가 있으면 라즈베리파이로 넘겨줍니다.
  if (Serial.available())
    mySerial.write(Serial.read());
}