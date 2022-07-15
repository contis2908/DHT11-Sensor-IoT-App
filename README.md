# The DHT11-Sensor for Temperature and Humidity
The DHT11 Sensor consists of a temperature and humidity sensor with a calibrated digital signal output. This App reads the humidity and temperature of a connects DHT-11 Sensor with a RaspberryPi Zero. The data is published together with time and device information to the specified Reswarm topic and can be subscribed to with the Record Evolution Data Studio.

Measurement Range for Temperature between 0 and 50 Degree Celcius \
Measurement Range for Humidity between 0 and 100


## Available Environment Variables
Write \
    **TOPIC**                  the Reswarm topic the data is published to

Read \
    **DEVICE_NAME**            current device's name (could change) \
    **DEVICE_SERIAL_NUMBER**   the unique identifier of the device (is immutable) \
    **SWARM_KEY**              the unique key of the swarm


## Publish 
Default name of Topic: _**reswarm.sensorData**_

    "timestamp": datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
    "device_name": device_name,
    "serial_number": serial_number,
    "data": [float(format(humidity,'0.1f')), float(format(temperature,'0.1f'))]

### MIT
Copyright (c) 2021 Record Evolution GmbH \
See license file on the source code
