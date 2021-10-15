# Test
Im folgenden testen wir die Verbindung vom Client (unteres Terminal) zum Server.
Dazu senden wir mit einem Mosquitto Client eine Test-Nachricht an den Broker.

Die Client Pakete müssen zuvor mit folgendem Befehl installiert werden:
`apt-get install -y mosquitto-clients`{{execute HOST2}}
Für die bessere Übersicht leeren wir wieder den Inhalt des Terminals
`clear`{{execute HOST2}}

Bevor nun der Test stattdindet muss der Begriff des "Topics" geklärt werden.
In der Einleitung wurde erwähnt, dass einem Broker mehrere Geräte und Datenstände gesendet werden können.

MQTT unterscheidet in den Daten mithilfe von Topics. Vorstellen kann man sich diese wie eine Verzeichnissstruktur.




Nun lassen wir uns im oberen Terminal die LOG-Dateien des MQTT Brokers anzeigen:
`tail -f /var/log/mosquitto/mosquitto.log`{{execute HOST2}}
 
Sind alle Vorkehrungen getroffen senden wir eine Testnachricht vom Client zum Broker.
Dies wird mit mosquitto_pub(lish) erledigt. mit -h wird der Host angegeben. -i ist der Bezeichner des Clients.
-t ist das sogenannte Topic
`mosquitto_pub -h [[HOST_IP]] -i Heizung -t test -m "{\"value1\":20,\"value2\":40}"`{{execute HOST2}}