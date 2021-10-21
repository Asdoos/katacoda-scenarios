Nun sendet unser "Fenstersensor" jede Minute zufällig ein "ich bin offen" oder "ich bin geschlossen" an den Broker.
Unsere Heizung weiß davon noch nichts und das möchten wir nun ändern.
Dafür wird der Begriff der Subscription eingeführt.

## Subscription
Die zweite Funktion eines MQTT Clients, neben dem Publishen von Werten, ist das subscriben, also abonnieren, von ausgewählten Werten.
Hier kommen erneut die Topics ins spiel. Der Client meldet dem Broker, dass er ein Topic abonnieren möchte. Dieser bestätigt oder verweigert die Anfrage.

Wird nun auf dem abonnierten Topic ein neuer Wert gepublisht sendet der Broker ebenfalls ein Publish weiter an die abonnierten Clients.
![MQTT Subscription](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/subscribe_flow.gif)

Der Client erhält dieses Publish und kann darauf reagieren.

Diese Funktion machen wir uns in unserem Szenario zu Nutze. Unser Heizungsclient abonniert das Topic des Fensters. Wird das Topic aktualisiert bekommt die Heizung vom Broker den neuen Wert zugesendet und schaltet ab, ein oder macht einfach nichts. Ändert sich der Zustand der Heizung wird dies wiederrum dem Broker auf dem Heizungstopic mitgeteilt, falls ein anderer Client diesen abonniert hat und mit dem Wert arbeitet.

## Heizungsclient

Das Programm für den Heizungsclient ist ebenfalls im Ordner /scripts/:
`cd /scripts/`{{execute HOST2}}
Es muss erneut der Broker gesetzt werden:
`vim heizung.py`{{execute HOST2}}
Die IP bleibt dabei die Selbe:
`[[HOST_IP]]`{{execute HOST2}}

Der Ablauf des Programms ist wie folgt:
Beim ersten Start verbindet sich der Client mit dem Broker und meldet an, das Topic des FensterSensors abonnieren zu wollen.
Ist dies erfolgreich wird ein Loop gestartet der neue Nachrichten des Brokers prüft und darauf wird reagiert.

Es müssen zuerst wieder die allgemeinen Parameter konfiguriert werden und der MQTT Client erstellt werden
```
pub_topic = u"Zuhause/Schlafzimmer1/HeizungStatus"
sub_topic = u"Zuhause/Schlafzimmer1/FensterStatus"
heizung_status = 1
broker = ""

client = mqtt.Client("HeizungSensor")
```

Im Code folgt anschließend die Funktion on_message(), welche steuert was bei einem eingehendenden Publish geschehen soll
In unserem Fall wird die erhaltene Nachricht ausgegeben. Dies dient im ersten Zweck der Information.
```
    print("=================== Neue Nachricht =====================")
    print("Wert: ", str(message.payload.decode("utf-8")))
    print("Topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    print("========================================================")
```
Nachfolgend wird je nach aktuellen Status der Heizung und des erhaltenen Status des Fensters eine Entscheidung getroffen, ob die Heizung ein oder ausgeschaltet wird.
```
    fenster_status = int(message.payload)
    if (heizung_status == 1 and fenster_status == 0) or (heizung_status == 0 and fenster_status == 1):
        return
    elif heizung_status == 1 and fenster_status == 1:
        print("Heizung wird abgeschaltet...")
        print("========================================================")
        publish_value(0)
    elif heizung_status == 0 and fenster_status == 0:
        print("Heizung wird eingeschaltet...")
        print("========================================================")
        publish_value(1)
```

Die Funktion publish_value ist identisch zu der aus dem Fenster Sensor

In der Main-Funktion wird der erstellte Client mit der on_message Funktion konfiguriert und die Verbindung hergestellt.
Danach kann das Topic abonniert werden und der initiale Status der Heizung gesendet werden (Eingeschaltet).
Die Loop ruft alle 5 Sekunden die Dunktion client.loop_start() auf welches den Client auffordert die Nachrichten zu prüfen.


```
client.on_message = on_message
client.connect(broker)
client.subscribe(sub_topic)
publish_value(heizung_status)
while True:
    print("Looping...")
    try:
        client.loop_start()
    except Exception as error:
        print(error)
    time.sleep(5)

```
Somit sind die Einrichtungsschritte erledigt.