# The DHT11-Sensor for Temperature and Humidity
The DHT11 Sensor consists of a temperature and humidity sensor with a calibrated digital signal output. This App reads the humidity and temperature of a connected DHT-11 Sensor from a RaspberryPi Zero. The measurement data is published together with time and device information to the specified topic and can be subscribed to with the Record Evolution Data Studio. The topic and the publishing interval can be adjusted via the environment variables that are exposed to the app user.

Measurement Range for Temperature between 0 and 50 Degree Celcius \
Measurement Range for Humidity between 0 and 100


## Available Environment Variables
#### Write
    TOPIC_PUB: the topic the data is published to
    Default: "reswarm.sensorData"

    LOOP_TIME: the publishing interval
    Default: "5" seconds

#### Read
    DEVICE_NAME: current device name (could change)
    DEVICE_SERIAL_NUMBER: the unique identifier of the device (is immutable)
    SWARM_KEY: the unique key of the swarm


## Publish 
Default name of Topic: _**reswarm.sensorData**_

    "timestamp": datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
    "device_name": device_name,
    "serial_number": serial_number,
    "humidity": float(format(humidity,'0.1f')),
    "temperature": float(format(temperature,'0.1f'))

### MIT
Copyright (c) 2021 Record Evolution GmbH \
See license file on the source code