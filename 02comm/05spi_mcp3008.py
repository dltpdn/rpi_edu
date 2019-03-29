import spidev, time

spi = spidev.SpiDev()
spi.open(0,0) #device:0, bus(slave) : 0
spi.max_speed_hz = 10000

def analog_read(channel):
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1]&3) << 8) + ret[2]
    print(ret)
    return adc_out
try:
    while True:
        reading = analog_read(0)
        voltage = reading * 3.3 / 1023
        print(("Reading=%d\tVoltage=%f" % (reading, voltage)))
        time.sleep(0.5) 
finally:
    spi.close()  
    
