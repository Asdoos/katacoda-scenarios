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
`sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa`{{execute "T1"}}

