Im folgenden testen wir die Verbindung vom Client (unteres Terminal) zum Server.
Dazu senden wir mit einem Mosquitto Client eine Test-Nachricht an den Broker.

## MQTT Client
Die Client Pakete müssen zuvor mit folgendem Befehl installiert werden:
`apt-get install -y mosquitto-clients`{{execute HOST2}}
Für die bessere Übersicht leeren wir wieder den Inhalt des Terminals
`clear`{{execute HOST2}}

Bevor nun der Test stattfindet muss der Begriff des "Topics" geklärt werden.
In der Einleitung wurde erwähnt, dass einem Broker mehrere Geräte und Datenstände gesendet werden können.
(vgl. [4] Using The Mosquitto_pub and Mosquitto_sub MQTT Client Tools)

## Topics
MQTT unterscheidet in den Daten mithilfe von Topics. Vorstellen kann man sich diese wie eine Verzeichnissstruktur.
Möchte der Sensor dem Broker einen Wert senden, muss dieser ein zugehöriges Topic angeben unter dem der Wert gespeichert wird.
In unserem Szenario könnte man die Topics wie folgt wählen:

Für das Fenster:
Zuhause/Schlafzimmer1/FensterStatus

Für die Heizung:
Zuhause/Schlafzimmer1/HeizungStatus

Für einen Wasserkocher in der Küche kann man die 2. Stufe anpassen:
Zuhause/Kueche/Wasserkocher

![MQTT Topics](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/mqtt-topics.png)

Mit dem neu gewonnenen Wissen über Topics können wir nun den Test durchführen.
(vgl. [5] Kommunikationsprotokolle)

## Verbindungstest
Zuerst lassen wir uns im oberen Terminal die LOG-Dateien des MQTT Brokers anzeigen. In diesen sieht man alle Anfragen von Clients zum Broker:
`tail -f /var/log/mosquitto/mosquitto.log`{{execute HOST1}}
 
Sind alle Vorkehrungen getroffen senden wir eine Testnachricht vom Client zum Broker.
Dies wird mit mosquitto_pub(lish) erledigt. Mit dem Parameter -h wird der Host angegeben, -i ist der Bezeichner des Clients und
-t ist das Topic
`mosquitto_pub -h [[HOST_IP]] -i Heizung -t Zuhause/Test/Temperatur -m "20"`{{execute HOST2}}

Gesendet wird also der Wert 20 an das Topic "Zuhause/Test/Temperatur" von dem Client mit der Bezeichnung "Heizung" und der Broker bestätigt diese Veröffentlichung.
![MQTT Publish](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/mqtt-publish.png)

Im Log sollten nun Zeilen geschrieben werden, dass sich ein Client namens "Heizung" verbunden und wieder getrennt hat.
Damit ist die Verbindung erfolgreich und wir können das Terminal leeren:
`clear`{{execute HOST2}}

(vgl. [4] Using The Mosquitto_pub and Mosquitto_sub MQTT Client Tools)