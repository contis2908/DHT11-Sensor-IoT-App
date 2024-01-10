import Adafruit_DHT
import time
import os
import asyncio
from asyncio import sleep
from datetime import datetime
from reswarm import Reswarm
import random

# Get environment variables
device_name = os.environ['DEVICE_NAME']
serial_number = os.environ['DEVICE_SERIAL_NUMBER']
topic_pub = os.environ.get('TOPIC_PUB', 'reswarm.sensorData')
loop_time = int(os.environ.get('LOOP_TIME', 5))
demo_data = os.environ.get('DEMO_DATA')

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

rw = Reswarm()

async def main():

    while True:
        randomTemp = None
        randomHumi = None
        humidity = None
        temperature = None

        if demo_data:
            print("Use demo_data ", demo_data)
            randomTemp = random.randint(20, 30)
            randomHumi = random.randint(40, 80)
        else:
            print("Use sensor data ", demo_data)
            try:
                humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            except Exception as e:
                print("Error: Problem reading data from sensor... ", e)

        if humidity is not None and temperature is not None or randomHumi is not None and randomTemp is not None:
            now = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            # print(f"{now} NOW Publish - Temp: {temperature:0.2f}C  Humidity: {humidity:0.2f}% Topic: {topic_pub}")
            data = {
                "timestamp": now,
                "device_name": device_name,
                "serial_number": serial_number,
                "humidity": float(format(humidity or randomHumi,'0.1f')),
                "temperature": float(format(temperature or randomTemp,'0.1f'))
            }

            try:
                # result = await rw.publish(topic_pub, data)
                await rw.publish_to_table("sensordata", data)
                print(f'Data was published: {data}')
            except Exception as e:
                print("Error: publish ... ", e)
                pass

        else:
            print("Error: No value for Humidity and Temperature - skip publish");
        
        await sleep(loop_time)

   
if __name__ == "__main__":
    # run the main coroutine
    asyncio.get_event_loop().create_task(main())
    # run the reswarm component
    rw.run()



            