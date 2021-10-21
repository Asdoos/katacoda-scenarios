# Der erste Schritt!
In einer Client-Server Struktur werden, wie im Namen zu erkennen, ein Server und ein Client benötigt.
Die zwei Terminals sollen diese Struktur repräsentieren.
Das System des obere Terminal soll unser MQTT Broker werden, welcher die Anfragen bearbeitet.
Im unteren werden die Clients simuliert. Ein Script im Hintergrund wird später alle Minute einen Status erzeugen, welches das Fenster simuliert.
Ein anderes wird den Heizungsregler simulieren und deren Reaktion ausgeben.

ACHTUNG: Auch wenn beide Scripts auf dem selben System ausgeführt werden soll die Kommunikation dennoch über den MQTT Broker geschehen!

## Installation MQTT Broker
Der bekannteste und freie Broker nennt sich "Mosquitto". Und wird wie folgt installiert:
Zuerst wird das Repository eingebunden:
`sudo apt-add-repository -y ppa:mosquitto-dev/mosquitto-ppa`{{execute "T1"}}

Anschließend kann Mosquitto über den Paket-Manager installiert werden:
`sudo apt-get install -y mosquitto`{{execute "T1"}}

Für eine bessere Übersicht leeren wir den Inhalt des Terminals
`clear`{{execute "T1"}}

Damit ist der Server schon installiert und kann Anfragen entgegen nehmen.
Eine weitere Konfiguration ist in diesem Scenario nicht weiter erforderlich. Der Broker nutzt den Standardport 1883 und nimmt Anfragen ohne Authentifizierung entgegen.

Weiter geht es im nächsten Schritt!
