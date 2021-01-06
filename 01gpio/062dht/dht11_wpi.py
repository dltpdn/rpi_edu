import wiringpi as wpi, time

def read_dht(pin):
	data  = [0,0,0,0,0]
	wpi.wiringPiSetupGpio()
	wpi.pinMode(pin, wpi.OUTPUT)
	wpi.digitalWrite(pin, wpi.HIGH)
	time.sleep(0.5)
	wpi.digitalWrite(pin, wpi.LOW)
	time.sleep(0.018)
	wpi.pinMode(pin, wpi.INPUT)
	wpi.pullUpDnControl(pin, wpi.PUD_UP)
	time.sleep(0.000001)

	old_val = -1
	for i in range(83): # 40*2 + 3
		time_s = time.time()
		while(True):
			val = wpi.digitalRead(pin)
			duration = time.time() - time_s
			if val == old_val:
				if duration > 0.001 :
					return (None, None, "error:timeout")
			else:
				if i >= 3 and old_val ==1:
					index = (i-3)//16
					data[index] <<=1
					if duration > 0.000048:
						data[index] |= 1
				old_val =val
				break

	if(data[4]== (data[0]+data[1]+data[2]+data[3])):
		humi = data[0] + data[1]/10.0
		temp = data[2] +data[3]/10.0
		return (humi, temp, "OK")
	else:
		return (None, None, "error:checksum")


PIN_DHT11=18
while(True):
    humi, temp, msg = read_dht(PIN_DHT11)
    if humi is None or temp is None :
        print(msg)
    else:
        print(f'huminity:{humi}%, temperature:{temp}*C')