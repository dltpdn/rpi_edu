# sudo pip3 install Adafruit_DHT 
import Adafruit_DHT

PIN_DHT11 = 18
while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN_DHT11)
    if humidity is not None and temperature is not None:
        print(f"humidity={humidity:.1f}%, temperature:{temperature:0.1f}*C")
    else:
        print("error.")