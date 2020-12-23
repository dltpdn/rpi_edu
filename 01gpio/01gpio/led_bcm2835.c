#include <bcm2835.h>
#include <stdio.h>

#define PIN RPI_GPIO_P1_12 //(which is GPIO 18)
int main(int argc, char **argv){
    if (!bcm2835_init())      return 1;
    bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_OUTP);
    int i;
    for(i=0; i<10; i++){
        // Turn it on
        bcm2835_gpio_write(PIN, HIGH);
        printf("pin %d HIGH\n" , PIN);
        // wait a bit
        bcm2835_delay(500);
        // turn it off
        bcm2835_gpio_write(PIN, LOW);
        printf("pin %d Low\n" , PIN);
        // wait a bit
        bcm2835_delay(500);
    }
    bcm2835_close(); 
    return 0;
}
