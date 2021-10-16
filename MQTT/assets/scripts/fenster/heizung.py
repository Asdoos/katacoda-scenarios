# Code inspiriert von http://www.steves-internet-guide.com/into-mqtt-python-client/
import paho.mqtt.client as mqtt

pub_topic = u"Zuhause/Schlafzimmer1/HeizungStatus"
sub_topic = u"Zuhause/Schlafzimmer1/FensterStatus"
broker = ""

client = mqtt.Client("HeizungSensor")


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


"""
Sendet einen übergebenen Wert an den MQTT Broker
"""


def publish_value(value):
    client.publish(pub_topic, value)


if __name__ == '__main__':
    client.on_message = on_message  # attach function to callback
    client.connect(broker)
    client.subscribe(sub_topic)
    client.loop_start()
