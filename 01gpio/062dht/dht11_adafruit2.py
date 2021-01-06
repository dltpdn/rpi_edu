# https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
# sudo pip3 install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2

import adafruit_dht, time

dht = adafruit_dht.DHT11(18)
while True:
    t = dht.temperature
    h = dht.humidity
    print(f'humidity:{h:.1f}%, temperature:{t:.1f}*C')
    time.sleep(1)
