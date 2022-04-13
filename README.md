# Hello World App
This is a simple "hello world" app to test on devices.
It logs some example output to the device console every second.
You can use this as a template to build your own IoT app.
You can also use any other programming language than the nodejs example in this example.

## Prerequisits
Each app must have a Dockerfile called "Dockerfile" in the top folder.
(see: https://docs.docker.com/engine/reference/builder/) and a base code written in your favorite programming language.
If you want to expose parameters of your app to users of this app you can add a file "env-template" to your top folder.
the contents of that file will be rendered as a nice form for users to fill in at their device-group.

### To build the source code:
Choose a device in the dropdown list in the side bar of the development studio and press "Build".
This effectively sends your code over to the chosen device and builds the app image directly on your device.
If you now press "Run" then the app will be executed on your device.
Now you can observe the log output of your app in the log panel below.

### Publishing an app:
If you are happy with your app, you can publish the app to the central App Registry so it can be used on other devices than the chosen development device.
You can do this in the publication menu in the app settings.

## Available Environment Variables
Frequently your app needs to identify the device that it is running on. For this and other purposes standard
environment variables are provided to the app.
* **DEVICE_NAME**            current device's name (could change)
* **DEVICE_SERIAL_NUMBER**   the unique identifier of the device (is immutable)
* **SWARM_KEY**              the unique key of the swarm

## Data volumes
If your app saves data on the device this data will not be retained accross app or device restarts.
There are two special folders you can use to persist data accross restarts.
* **/data** A folder that is private to your app. Other apps can not access it's content.
* **/shared** A folder that is shared by all apps on the device.

## Hardware access
You app may want to interact with hardware like sensors that is attached to your device.
These accessories are provided as mount points in a unix system. These are the ones that are available
on a Raspberry Pi for example.

* ````  /dev/ttyUSB0     ````    For GSM Mobile Huawei LTE USB-Stick
* ````  /dev/ttyUSB2     ````    For SIM7600E-H 4G HAT GPS, phone calls, SMS
* ````  /dev/cdc-wdm0    ````    For SIM7600E-H mobile network
* ````  /dev/ttyS0       ````    For GPS Module
* ````  /dev/ttyAMA0     ````    For the Sigfox devices
* ````  /dev/ppp         ````    For the PPP network interface unit
* ````  /dev/snd         ````    For Audio Module
* ````  /dev/spidev0.0   ````    For SPI (LED Matrix)
* ````  /dev/spidev0.1   ````    For SPI (LED Matrix)
* ````  /dev/mem         ````    For LED 7 Colors
* ````  /dev/usb         ````    For general USB usage
* ````  /dev/i2c-0       ````    For I2C interface 0
* ````  /dev/i2c-1       ````    For I2C interface 1
* ````  /dev/gpiomem     ````    For GPIO device

# LICENSE
### MIT
Copyright (c) 2021 Record Evolution GmbH
See license file on the source code
