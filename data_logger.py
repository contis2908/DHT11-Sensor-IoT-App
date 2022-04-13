import Adafruit_DHT
import time
import os
from datetime import datetime

from autobahn.twisted.component import Component, run
from autobahn.wamp.types import PublishOptions
from twisted.internet.defer import inlineCallbacks
from twisted.internet.task import LoopingCall
from autobahn.twisted.util import sleep
from twisted.internet import reactor

# # Get environment variables
TOPIC_PREFIX = os.environ.get('TOPIC_PREFIX', 'reswarm.tempHmd')
DATA_LOG_INTERVAL = float(os.environ.get('DATA_LOG_INTERVAL', 10.0))
device_name = os.environ['DEVICE_NAME']
serial_number = os.environ['DEVICE_SERIAL_NUMBER']

pub_topic = TOPIC_PREFIX + '.' + serial_number

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4


def measure():
    try:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    except:
        print("Error: Problem reading data from sensor...")

    return humidity, temperature




comp = Component(
    transports={
                "type": "websocket",
                "url": "ws://cb.reswarm.io:8088",
                "max_retries": -1,
                "max_retry_delay": 2,
                "initial_retry_delay": 0.5,
                # "autoping_interval": 2,
                # "autoping_timeout": 4
                },
    realm=u"userapps",
    authentication={
        u"wampcra": {
            u'authid': os.environ['DEVICE_SERIAL_NUMBER'],
            u'secret': os.environ['DEVICE_SERIAL_NUMBER']
        }
    },
)

@comp.on_join
@inlineCallbacks
def onJoin(session, details):
    print("Session: {} - Details: {}".format(session, details))
    print("publishing to " + pub_topic)
    while True:
        try:
            humidity, temperature = measure()
        except:
            humidity, temperature = ""

        if humidity is not None and temperature is not None:
            print("Temp: {0:0.1f}C  Humidity: {1:0.1f}%".format(temperature, humidity))

            toPublish = result_dict = {
                "timestamp": datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                "device_name": device_name,
                "serial_number": serial_number,
                "data": [format(humidity,'0.1f'), format(temperature,'0.1f')]
            }

            try:
                session.publish(pub_topic, toPublish)
            except:
                pass

        else:
            print("Error: No value for Humidity and Temperature - skip publish");
            
        yield sleep(DATA_LOG_INTERVAL)
    

@comp.on_leave
def onLeave(session, details):
    print('onLeave...')
    session.disconnect()


@comp.on_disconnect
def onDisconnect(session, was_clean):
    print('onDisconnect...')

@comp.on_connectfailure
def onConnectfailure(session, was_clean):
    print('onConnectfailure...')

if __name__ == "__main__":
    run([comp])


            