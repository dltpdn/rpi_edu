#if 0
#define PERI_BASE        0x20000000  //Pi 1(BCM2835)
#else
#define PERI_BASE        0x3F000000  //Pi 2+(BCM2836+)
#endif

#define GPIO_BASE                (PERI_BASE + 0x200000) /* GPIO controller */
#define GPIO_SIZE				(256)  // GPIO Registor size,  0x7E200B0 - 0x7E2000000 + 14 = 180
#if 0
#define MMAP_DEV			"/dev/mem"  //for root
#else
#define MMAP_DEV			"/dev/gpiomem"  //root less, for gpio group
#endif

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

int  mem_fd;
void *gpio_map;
volatile unsigned *gpio;

// datasheet p.90~
#define GPIO_IN(pin) (*(gpio+((pin)/10)) &= ~(7<<(((pin)%10)*3)))  // set direction to in
#define GPIO_OUT(pin) (*(gpio+((pin)/10)) |=  (1<<(((pin)%10)*3))) // set direction to out
#define GPIO_SET(pin) (*(gpio+7) = 1<<pin)  // set,   HIGH
#define GPIO_CLR(pin) (*(gpio+10) = 1<<pin) // clear, LOW


int main(int argc, char **argv){
  int pin = 18, i=0;

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
     printf("mmap error %d\n", (int)gpio_map);//errno also set!
     exit(-1);
  }

  gpio = (volatile unsigned *)gpio_map;

  GPIO_OUT(pin);
  printf("pin%d was set OUT.\n");
  for(i = 0; i<5; i++){
	  GPIO_SET(pin);
	  printf("pin%d On\n", pin);
	  sleep(1);
	  GPIO_CLR(pin);
	  printf("pin%d Off\n", pin);
	  sleep(1);
  }

	munmap(gpio_map, GPIO_SIZE);
	close(mem_fd);
  return 0;
} // main


/* for compile and run
$ gcc -o  gpio_register gpio_register
$ sudo ./gpio_register.c
*/
