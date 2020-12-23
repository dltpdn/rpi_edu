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

#define HIGH 1
#define LOW 0

int  mem_fd;
void *gpio_map;
volatile unsigned *gpio;

void init();
void setOut(int pin);
void output(int pin, int value);