#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include "led_lib.h"

void init(){
    if ((mem_fd = open(MMAP_DEV, O_RDWR|O_SYNC) ) < 0) {
        printf("can't open /dev/mem \n");
        exit(-1);
    }

    gpio_map = mmap(
        NULL,             // Any adddress in our space will do
        GPIO_SIZE,       // Map length
        PROT_READ|PROT_WRITE,// Enable reading & writting to mapped memory
        MAP_SHARED,       // Shared with other processes
        mem_fd,           // fd to map
        GPIO_BASE         // Offset to GPIO peripheral
    );
    close(mem_fd); //No need to keep mem_fd after opening mmap

    if (gpio_map == MAP_FAILED) {
        printf("mmap error %d\n", (char *)gpio_map);//errno also set!
        exit(-1);
    }

    gpio = (volatile unsigned *)gpio_map;    
}

// datasheet p.90~
// set GPIO direction to out
void setOut(int pin){
    *(gpio+((pin)/10)) =  (1<<(((pin)%10)*3));
}

void output(int pin, int value){
    if(value == LOW){
        *(gpio+10) = 1<<pin; // set GPIO to HIGH
    }else if(value == HIGH){
        *(gpio+7) = 1<<pin; // set GPIO to LOW
    }
}

/* for compiling as shared object
$ gcc led_lib.c -o led_lib.so -shared -fPIC
*/