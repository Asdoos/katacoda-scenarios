# Code inspiriert von https://www.eclipse.org/paho/index.php?page=clients/python/index.php

import random
import paho.mqtt.client as mqtt

topic = u"Zuhause/Schlafzimmer1/FensterStatus"
broker = ""

client = mqtt.Client()


def gen_value() -> int:
    return random.randint(0, 1)


"""
Sendet einen übergebenen Wert an den MQTT Broker
"""


def publish_value(value: int):
    client.connect(broker)
    client.publish(topic, value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    publish_value(gen_value())
