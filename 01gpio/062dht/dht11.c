#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <wiringPi.h>

#define DHT_MAXCOUNT 32000
#define DHT_PULSES 41
#define DHT_ERROR_TIMEOUT -1
#define DHT_ERROR_CHECKSUM -2
#define DHT_ERROR_ARGUMENT -3
#define DHT_ERROR_GPIO -4
#define DHT_SUCCESS 0

int read_dht(int pin, float* humidity, float* temperature) {
  if (humidity == NULL || temperature == NULL) {
    return DHT_ERROR_ARGUMENT;
  }
  *temperature = 0.0f;
  *humidity = 0.0f;

  if(wiringPiSetupGpio() <0){
    return DHT_ERROR_GPIO;
  }

  int pulseCounts[DHT_PULSES*2] = {0};

  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);
  delay(500);
  digitalWrite(pin, LOW);
  delay(20);

  pinMode(pin, INPUT);
  delayMicroseconds(1);
  int count = 0;
  while (digitalRead(pin)) {      
    if (++count >= DHT_MAXCOUNT) {
      return DHT_ERROR_TIMEOUT;
    }
  }

  for (int i=0; i < DHT_PULSES*2; i+=2) {
    while(!digitalRead(pin)){
      if (++pulseCounts[i] >= DHT_MAXCOUNT) {
        return DHT_ERROR_TIMEOUT;
      }
    }
    while(digitalRead(pin)){
      if (++pulseCounts[i+1] >= DHT_MAXCOUNT) {
        return DHT_ERROR_TIMEOUT;
      }
    }
  }

  int threshold = 0;
  for (int i=2; i < DHT_PULSES*2; i+=2) {
    threshold += pulseCounts[i];
  }
  threshold /= DHT_PULSES-1;

  uint8_t data[5] = {0};
  for (int i=3; i < DHT_PULSES*2; i+=2) {
    int index = (i-3)/16;
    data[index] <<= 1;
    if (pulseCounts[i] >= threshold) {
      data[index] |= 1;
    }
  }

  if (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF)) {
    *humidity = (float)data[0] + data[1]/10.0;
    *temperature = (float)data[2] +data[3]/10.0;
    return DHT_SUCCESS;
  }
  else {
    return DHT_ERROR_CHECKSUM;
  }
}

int main(){
	while (1) {
        int pin = 18;
        float  humidity = 0, temperature = 0; 
		int ret = read_dht(pin, &humidity, &temperature);
        if(ret){
            printf("error:%d\n", ret);
        }else{
            printf("humidity:%.1f%%, temperature:%.1f*C\n", humidity, temperature);
        }
	}
}