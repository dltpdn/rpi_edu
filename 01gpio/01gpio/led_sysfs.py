import time

pin_gpio = 18
f = open('/sys/class/gpio/export', 'w')
f.write(str(pin_gpio))
f.close()
print('export done.')

f = open('/sys/class/gpio/gpio%d/direction'%pin_gpio, 'w')
print('direction done')
f.write('out')
f.close()

f = open('/sys/class/gpio/gpio%d/value'%pin_gpio, 'w')
for i in range(10):
    f.write(str(1))
    f.flush()
    print('set value 1.')
    time.sleep(0.5)
    f.write(str(0))
    f.flush()
    print('set value 0.')
    time.sleep(0.5)
f.close()

f = open('/sys/class/gpio/unexport', 'w')
f.write('%d'%pin_gpio)
f.close()
print('unexport done.')
