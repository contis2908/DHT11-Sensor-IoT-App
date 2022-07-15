import Adafruit_DHT
import time
import os
from asyncio import sleep
from datetime import datetime
from asyncio.events import get_event_loop
from reswarm import Reswarm

# Get environment variables
TOPIC_PREFIX = os.environ.get('TOPIC_PREFIX', 'reswarm.sensorData')
DATA_LOG_INTERVAL = float(os.environ.get('DATA_LOG_INTERVAL', 10.0))
device_name = os.environ['DEVICE_NAME']
serial_number = os.environ['DEVICE_SERIAL_NUMBER']
pub_topic = TOPIC_PREFIX
loop_time = os.environ['LOOP_TIME']
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

async def main():

    while True:

        humidity = ''
        temperature = ''

        try:
            print("measure...")
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            print("Temp: {0:0.1f}C  Humidity: {1:0.1f}%".format(temperature, humidity))
            
        except:
            print("Error: Problem reading data from sensor... ")

        if humidity is not None and temperature is not None:
            # print("Now Publish - Temp: {0:0.1f}C  Humidity: {1:0.1f}%".format(temperature, humidity))

            data = {
                "timestamp": datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                "device_name": device_name,
                "serial_number": serial_number,
                "humidity": float(format(humidity,'0.1f')),
                "temperature": float(format(temperature,'0.1f'))
            }

            try:
                rw = Reswarm(serial_number=serial_number)
                result = await rw.publish(pub_topic, data)
            except:
                print("Error during publish");
                pass

        else:
            print("Error: No value for Humidity and Temperature - skip publish");
        
        await sleep(int(loop_time))

   
            

if __name__ == "__main__":
    get_event_loop().run_until_complete(main())



            