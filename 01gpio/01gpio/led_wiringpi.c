#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

//#define LED 1 // BCM18
#define LED 18
int main( void) {
        int i;

        //wiringPiSetup();
        wiringPiSetupGpio();
        pinMode(LED, OUTPUT);
        for(i=0; i<10; i++){
               digitalWrite(LED, HIGH);
               printf("pin %d HIGH\n" , LED);
               delay(1000);
               digitalWrite(LED, LOW);
               printf("pin %d LOW\n" , LED);
               delay(1000);
       }
        return EXIT_SUCCESS;
}


/*
$ gcc –o wiringpi_led wiringpi_led.c –lwiringPi
$ sudo ./wiringpi_led

*/
