import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    try:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    except:
        print("Error: Problem reading data...")
        humidity, temperature = ""

    if humidity is not None and temperature is not None:
        print("Temp: {0:0.1f}C  Humidity: {1:0.1f}%".format(temperature, humidity))
    else:
        print("Error: No value for Humidity and Temperature");
    time.sleep(3);



            