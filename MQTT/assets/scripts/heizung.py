# Code inspiriert von http://www.steves-internet-guide.com/into-mqtt-python-client/
import time

import paho.mqtt.client as mqtt

pub_topic = u"Zuhause/Schlafzimmer1/HeizungStatus"
sub_topic = u"Zuhause/Schlafzimmer1/FensterStatus"
heizung_status = 1
broker = ""

client = mqtt.Client("HeizungSensor")


def on_message(client, userdata, message):
    fenster_status = message.payload.decode("utf-8") == 0
    print(type(fenster_status))
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

    #Heizung: 0 AUS, 1 AN
    #Fenster: 0 ZU, 1 AUF

    #0 0 -> Heizung an
    #0 1 -> Nichts tun
    #1 0 -> Nichts tun
    #1 1 -> Heizung aus

    if (heizung_status == 1 and fenster_status == 0) or (heizung_status == 0 and fenster_status == 1):
        return
    if heizung_status == 1 and fenster_status == 1:
        print("Heizung wird abgeschaltet...")
        publish_value(0)
    if heizung_status == 0 and fenster_status == 0:
        print("Heizung wird eingeschaltet...")
        publish_value(1)

"""
Sendet einen übergebenen Wert an den MQTT Broker
"""


def publish_value(value):
    client.publish(pub_topic, value)


if __name__ == '__main__':
    client.on_message = on_message  # Funktion setzen, die verwendet werden soll
    client.connect(broker)
    client.subscribe(sub_topic)
    publish_value(heizung_status)                # Melde Status
    while True:
        print("Looping...")
        try:
            client.loop_start()
        except Exception as error:
            print(error)
        time.sleep(5)
