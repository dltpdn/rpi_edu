import wiringpi as wpi, time
pin	=18

wpi.wiringPiSetupGpio()

while True:
	data  = []
	data2 = []
	cnt = 0
	wpi.pinMode(pin, wpi.OUTPUT)
	wpi.digitalWrite(pin, wpi.HIGH)
	wpi.digitalWrite(pin, wpi.LOW)
	wpi.delay(18)
	wpi.pinMode(pin, wpi.INPUT)
	wpi.pullUpDnControl(pin, wpi.PUD_UP)


	while True:
		err = True
		while(wpi.digitalRead(pin)==0):
			pass
		old = time.time()
		while(wpi.digitalRead(pin) == 1 ):
			err = False
			end = time.time()
			if end - old > 0.001 :
				err = True
				break
		if err == False:
			data.append(end-old)
		cnt +=1
		if(cnt > 41):
			break
	#print data , len(data)
	
	if len(data) > 40 and data[0] >= 0.00008:
		data.pop(0)
		for i in data:
			if i >=0.00008:
				print 'no good data:invalid data'
				break
			elif i >= 0.00004 : #originally should be 70us
				data2.append(1)
			else:
				data2.append(0)
		#print data2, len(data2)
		if len(data2) !=  40:
			print 'no good data:not enough data.'
		else:
			humi1 =  int("".join(str(x) for x in data2[0:8]), 2)
			humi2 =  int("".join(str(x) for x in data2[9:16]), 2)
			temp1 = int("".join(str(x) for x in data2[17:24]), 2)
			temp2 =  int("".join(str(x) for x in data2[25:32]), 2)
			crc =  int("".join(str(x) for x in data2[33:40]), 2)
			if(crc != (humi1 + humi2 + temp1 + temp2)):
				print 'no good data:crc err'
			else:
				print 'huminity : %d.%d%%, temperatur:%d.%dC' %(humi1, humi2, temp1, temp2)
	
	else:
		print 'no good data'
	wpi.delay(100)