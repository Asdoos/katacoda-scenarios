# Code inspiriert von http://www.steves-internet-guide.com/into-mqtt-python-client/

import random
import time

import paho.mqtt.client as mqtt

topic = u"Zuhause/Schlafzimmer1/FensterStatus"
broker = ""

client = mqtt.Client("FensterSensor")


def gen_value() -> int:
    return random.randint(0, 1)


"""
Sendet einen ├╝bergebenen Wert an den MQTT Broker
"""


def publish_value(value: int):
    client.publish(topic, value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client.connect(broker)
    while True:
        print("Publish Value...")
        try:
            publish_value(gen_value())
        except Exception as error:
            print(error)
        time.sleep(60)
