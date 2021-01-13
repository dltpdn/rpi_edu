import spidev, time

spi = spidev.SpiDev()
spi.open(0,0) #device:0, bus(slave) : 0
spi.max_speed_hz = 1350000
channel = 0
try:
    while True:
        ret = spi.xfer2([1, (8 + channel) << 4, 0])
        value = ((ret[1]&3) << 8) + ret[2]
        volt = value * 3.3 / 1023
        print(f"bytes:{ret},\t value:{value},\t Volt:{volt:.2f}")
        time.sleep(0.5) 
finally:
    spi.close()  
    
