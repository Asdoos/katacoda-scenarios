#Test
Im folgenden testen wir die Verbindung vom Client (unteres Terminal) zum Server.
Dazu senden wir mit einem Mosquitto Client eine Test-Nachricht an den Broker.

Die Client Pakete müssen zuvor mit folgendem Befehl installiert werden:
`apt-get install mosquitto-clients`{{execute "T2"}}
und wieder mit Y bestätigen:
`y`{{execute "T2"}}

 
`mosquitto_pub -h [[HOST_IP]] -i Heizung -t test -m "{\"value1\":20,\"value2\":40}"`{{execute "T2"}}