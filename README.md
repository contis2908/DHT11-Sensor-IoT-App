# The DHT11-Sensor for Temperature and Humidity
The DHT11 Sensor consists of a temperature and humidity sensor with a calibrated digital signal output. This App reads the humidity and temperature of a connected DHT-11 Sensor from a RaspberryPi Zero. The measurement data is published together with time and device information to the specified topic and can be subscribed to with the Record Evolution Data Studio. The topic and the publishing interval can be adjusted via the environment variables that are exposed to the app user.

Measurement Range for Temperature between 0 and 50 Degree Celcius <br>
Measurement Range for Humidity between 0 and 100

<div style="display:flex;flex-direction:row;flex-wrap:wrap;">
    <img style="max-width:60%; margin:16px auto;" src="https://res.cloudinary.com/dotw7ar1m/image/upload/v1681308879/gpio_pi_zero_dht11.png">
    <img style="max-width:40%; margin:16px auto;" src="https://res.cloudinary.com/dotw7ar1m/image/upload/v1681996569/Screenshot_2023-04-20_at_15.16.22.png">
</div>

## Available Environment Variables

### _Write_
**TOPIC_PUB**: the topic the data is published to <br>
**Default**: "reswarm.sensorData"

**LOOP_TIME**: the publishing interval <br>
**Default**: "5" seconds

### _Read_
**DEVICE_NAME**: current device name (could change) <br>
**DEVICE_SERIAL_NUMBER**: the unique identifier of the device (is immutable) <br>
**SWARM_KEY**: the unique key of the swarm


## Publish 
    timestamp: datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
    device_name: device_name,
    serial_number: serial_number,
    humidity: float(format(humidity,'0.1f')),
    temperature: float(format(temperature,'0.1f'))

## MIT License
Copyright (c) 2021 Record Evolution GmbH <br>
See license file on the source code