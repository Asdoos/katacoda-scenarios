Herzlich Willkommen zu diesem kleinen Scenario.
## Beschreibung
Im Folgenden werden wir herausfinden, wie die Daten eines IOT Gerätes übertragen werden können.
Als Kommunikationsmethode wird dafür "MQTT" genutzt, eines der am meist verbreitesten Machine-to-Machine (M2M) Netzwerkprotokolle
## Vorraussetzung
Du solltest mit der Linux CLI vertraut sein. Grundsätzliche Dinge, wie beispielsweise das wechseln des Verzeichnisses, werden hier nicht erläutert und werden als gegeben gesehen.
Das genutze Scenario benötigt zur realen Durchführung geeignete Hardware. Diese Konfiguration wird hier jedoch nicht betrachtet.
## Scenario
Ein beliebter Anwendungsfall für IOT ist die Heim-Automatisierung. Verschiedene Sensoren sind im Wohnraum oder sogar im Garten verteilt. Die Variation an Sensoren ist dabei beinahe unbegrenzt. 
Beispiele wären heir die Temperaturen in den Räumen, Luftfeuchtigkeit, Sauerstoffgehalt, Wasserfluss der Heizung, Boilertemperatur, Fenster, Stromverbrauch von Elektrogeräten... 
Die Liste lässt sich beliebig erweitern.
Wir wollen nun eine gedachte Verbindung vom Fenster zur Heizung herstellen. Es ist ökologisch und ökonomisch nicht sehr sinnvoll zu heizen, wenn ein Fenster geöffnet ist.
Wie wäre es also wenn sich die Heizungen automatisch abstellen sobald ein Fenster im selben Raum geöffnet ist?
Dafür werden ein Sensor an dem Fenster und ein Aktor an der Heizung benötigt. Diese beiden müssen nun miteinander kommunizieren.
## MQTT
Wie funktioniert nun dieses "MQTT" überhaupt?!...
Zu erst muss erwähnt werden, dass MQTT (ausgeschrieben: Message Queuing Telemetry Transport) auf dem Client-Server Prinzip Funktioniert.
Es gibt also irgendwo ein Server der Anfragen entgegennimmt, verarbeitet und wieder versendet.
Nun gibt es im Normalfall nicht nur einen einzigen Sensor, der seine Daten senden möchte. 