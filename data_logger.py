import Adafruit_DHT
import time
import os
from asyncio import sleep
from datetime import datetime
from asyncio.events import get_event_loop
from reswarm import Reswarm

# Get environment variables
device_name = os.environ['DEVICE_NAME']
serial_number = os.environ['DEVICE_SERIAL_NUMBER']
topic_pub = os.environ.get('TOPIC_PUB', 'reswarm.sensorData')
loop_time = int(os.environ['LOOP_TIME'])

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

async def main():
    rw = Reswarm()

    while True:

        humidity = 0
        temperature = 0

        try:
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
        except Exception as e:
            print("Error: Problem reading data from sensor... ", e)

        if humidity is not None and temperature is not None:
            now = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{now} Publish - Temp: {temperature:0.1f}C  Humidity: {humidity:0.1f}% Topic: {topic_pub}")
            data = {
                "timestamp": now,
                "device_name": device_name,
                "serial_number": serial_number,
                "humidity": float(format(humidity,'0.1f')),
                "temperature": float(format(temperature,'0.1f'))
            }

            try:
                result = await rw.publish(topic_pub, data)
            except:
                print("Error during publish");
                pass

        else:
            print("Error: No value for Humidity and Temperature - skip publish");
        
        await sleep(loop_time)

   
if __name__ == "__main__":
    get_event_loop().run_until_complete(main())



            