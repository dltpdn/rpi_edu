import Adafruit_DHT

PIN_DHT11 = 18

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN_DHT11)
    
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to get reading.")