In diesem Schritt werden wir das Skript implementieren, welches im Hintergrund jede Minute einen Wert für das Fenster generiert.
Verwendet wird dafür die Sprache Phyton.

Ein vorgefertigtes Script liegt unter /scripts/fenster/
`cd /scripts/fenster/`{{execute HOST2}}

Schauen wir uns dies einmal an.
`vim main.py`{{execute HOST2}}

Genutzt wird die MQTT-Client Bibliothek Paho
```
import paho.mqtt.client as mqtt
``` 

Anschließend wird das Topic und der Broker festgelegt.
``` 
topic = u"Zuhause/Schlafzimmer1/FensterStatus"
broker = ""
```
Jedoch muss der Boker noch ausgefüllt werden. Trage hier die IP ein.
`[[HOST_IP]]`{{execute HOST2}}

Um die Bibliothek zu nutzen wird ein Client erstellt. Der angegebene Parameter entscpricht dem Namen des Clients.
```
client = mqtt.Client("FensterSensor")
```

Die Funktion gen_value() gibt einen zufälligen Wert zwischen 0 und 1 zurück.
0 steht dabei für ein geschlossenes Fenster, 1 für ein geöffnetes.

```
def gen_value() -> int:
    return random.randint(0, 1)
```

Die Main-Funktion benutzt gen_value() als Parameter für die publish_value() Funktion in der der Wert gesendet wird.
Diese stellt eine Verbindung zum Broker her und sendet (published) den generierten Wert an das zuvor festgelegte Topic.
```
def publish_value(value: int):
    client.connect(broker)
    client.publish(topic, value)
```

In der Main Funktion ist ein Loop eingebaut, der alle 60 Sekunden den Wert sendet.
```
    while True:
        print("Publish Value...")
        try:
            publish_value(gen_value())
        except Exception as error:
            print(error)
        time.sleep(60)
```
Ist die IP eingetragen kann das Skript gespeichert und geschlossen werden.

Testen wir einmal das Skript durch den Befehl:
`python3.8 main.py`{{execute HOST2}}

Wird kein Fehler angezeigt können wir das Programm im Hintergrund laufen lassen:
`nohup python3.8 main.py &`{{execute HOST2}}