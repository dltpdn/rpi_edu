#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main( int argc, char **argv) {
        int gpio_pin = 18;
        int fd;
        char buff[BUFSIZ];

       fd = open("/sys/class/gpio/export", O_WRONLY );
        if (fd == -1) {
               perror("fail to open export." );
               return 1;
       }
        sprintf(buff, "%d" , gpio_pin);
        if (write (fd, buff, sizeof(buff)) == -1) {
               perror("fail to export GPIO" );
               return 1;
       }
        close(fd);
	   
	   sprintf(buff, "/sys/class/gpio/gpio%d/direction" , gpio_pin);
       fd = open(buff, O_WRONLY);
        if (fd == -1) {
               perror("fail to open GPIO Direction File" );
               return 1;
       }
        if (write (fd, "out" , 4) == -1) {
               perror("fail to set direction\n" );
               return 1;
       }
        close(fd);
        sprintf(buff, "/sys/class/gpio/gpio%d/value" , gpio_pin);
       fd = open(buff, O_WRONLY);
        int i=0;
        for(i=0; i<10; i++) {
               if (write (fd, "1" , sizeof("1")) == -1) {
                      perror("fail to set value:1" );
                      return 1;
              }
               printf("set gpio %d value as HIGH\n", gpio_pin);
               sleep(1);
               if (write (fd, "0" , sizeof("0")) == -1) {
                      perror("fail to set value:0" );
                      return 1;
              }
               printf("set gpio %d value as LOW\n", gpio_pin);
               sleep(1);
       }
        close(fd);
        
        
        fd = open("/sys/class/gpio/unexport" , O_WRONLY );
        sprintf(buff, "%d" , gpio_pin);
        write(fd, buff, strlen(buff));
        close(fd);

        return 0;
}
       
       
/*
$ gcc –o gpioled gpioled.c
$ sudo ./gpioled
*/
