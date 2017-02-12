import spidev, time

spi = spidev.SpiDev()
spi.open(0,0) #bus:0, channel : 0

def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
   # r = spi.xfer2([1])
    adc_out = ((r[1]&3) << 8) + r[2]
    print r
    return adc_out
try:
    while True:
        reading = analog_read(0)
        voltage = reading * 3.3 / 1024
        print("Reading=%d\tVoltage=%f" % (reading, voltage))
        time.sleep(0.5) 
finally:
    spi.close()  
    
