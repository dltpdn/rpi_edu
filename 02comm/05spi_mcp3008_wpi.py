import wiringpi as wpi, time

speed = 1350000
fd = wpi.wiringPiSPISetup(0, speed)
channel = 0
while True:
    size, ret = wpi.wiringPiSPIDataRW(0,bytes([1, (8 + channel) << 4, 0]))
    print(size, ret)
    #value = ((ret[1]&3) << 8) + ret[2]
    value = int.from_bytes(ret, byteorder='big')
    volt = value * 3.3 / 1023
    print(f"bytes:{[b for b in ret]},\t value:{value},\t Volt:{volt:.2f}")
    time.sleep(0.5) 
    
