#include "led_lib.h"

int main(int argc, char **argv){
    int pin = 18, i=0;
    init();
    setOut(pin);
    printf("pin%d was set OUT.\n", pin);
    for(i = 0; i<5; i++){
        output(pin, HIGH);
        printf("pin%d On\n", pin);
        sleep(1);
        output(pin, LOW);
        printf("pin%d Off\n", pin);
        sleep(1);
    }

    munmap(gpio_map, GPIO_SIZE);
    close(mem_fd);
    return 0;
} // main
/* for compiling with shared object
$ gcc led_lib_main.c -o led_lib_main -l:led_lib -L.

for running 
$ LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH ./led_lib_main
*/