#if 0
#define BCM2708_PERI_BASE        0x20000000
#else
#define BCM2708_PERI_BASE        0x3F000000
#endif

#define GPIO_BASE                (BCM2708_PERI_BASE + 0x200000) /* GPIO controller */
#define GPIO_SIZE				(256)
#if 0
#define MMAP_DEV			"/dev/mem"
#else
#define MMAP_DEV			"/dev/gpiomem"
#endif

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

int  mem_fd;
void *gpio_map;

// I/O access
volatile unsigned *gpio;


// GPIO setup macros. Always use INP_GPIO(x) before using OUT_GPIO(x) or SET_GPIO_ALT(x,y)
#define GPIO_IN(g) (*(gpio+((g)/10)) &= ~(7<<(((g)%10)*3)))
#define GPIO_OUT(g) (*(gpio+((g)/10)) |=  (1<<(((g)%10)*3)))
#define GPIO_SET_ALT(g,a) *(gpio+(((g)/10))) |= (((a)<=3?(a)+4:(a)==4?3:2)<<(((g)%10)*3))

#define GPIO_SET(g) (*(gpio+7) = 1<<g)  // sets   bits which are 1 ignores bits which are 0
#define GPIO_CLR(g) (*(gpio+10) = 1<<g) // clears bits which are 1 ignores bits which are 0

#define GPIO_GET(g) (*(gpio+13)&(1<<g)) // 0 if LOW, (1<<g) if HIGH

#define GPIO_PULL *(gpio+37) // Pull up/pull down
#define GPIO_PULLCLK0 *(gpio+38) // Pull up/pull down clock

int main(int argc, char **argv)
{
  int pin = 18, i=0;

  if ((mem_fd = open(MMAP_DEV, O_RDWR|O_SYNC) ) < 0) {
     printf("can't open /dev/mem \n");
     exit(-1);
  }

  gpio_map = mmap(
     NULL,             //Any adddress in our space will do
     GPIO_SIZE,       //Map length
     PROT_READ|PROT_WRITE,// Enable reading & writting to mapped memory
     MAP_SHARED,       //Shared with other processes
     mem_fd,           //File to map
     GPIO_BASE         //Offset to GPIO peripheral
  );

  close(mem_fd); //No need to keep mem_fd open after mmap

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


/*
$ gcc –o  gpio_register gpio_register
$ sudo ./wiringpi_led

*/
