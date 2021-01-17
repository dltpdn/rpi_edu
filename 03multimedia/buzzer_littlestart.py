import wiringpi  
from time import sleep  
PIN_BUZ = 18

frequencies = {'c':262, 'd':294, 'e':330, 'f':349, 'g':392, 'a':440, 'b':494}
notes = 'ccggaag ffeeddc ggffeed ggffeed ccggaag ffeeddc'

wiringpi.wiringPiSetupGpio()  
try:
    wiringpi.softToneCreate(PIN_BUZ)
    for i in notes:
        if i != ' ':
            wiringpi.softToneWrite(PIN_BUZ, frequencies[i])
        else:
            wiringpi.softToneWrite(PIN_BUZ, 0)
        sleep(0.3)
finally:
    wiringpi.pinMode(PIN_BUZ, 0)
