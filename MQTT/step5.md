Im oberen Terminal siehst du nun LOG-Einträge. Es soll nun darum gehen, was diese aussagen.

- CONNACK: Wenn ein neuer Client sich verbindet sendet der Broker ein CONNACK(nowledge) an den Client zurück um die Verbindung zu bestätigten.
- SUBSCRIBE: Wenn ein Client ein TOPIC abonnieren möchte, sendet er ein SUBSCRIBE an den Broker
- SUBACK: Das Angeforderte SUBSCRIPTION wird vom Server an den Client bestätigt
- Recieve PUBLISH: Ein neuer Wert wurde von einem Client gesendet
- Sending PUBLISH: Ein neuer Wert wurde an ein Client gesendet
- PINGREQ: Ein Client sendet die Anfrage, ob der Broker noch aktiv ist
- PINGRESP: Rückgabe vom Broker, dass er noch aktiv ist

Im Schaubild ist veranschaulicht wie eine typische Kommunikation aussieht

![MQTT Ablauf](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/800px-MQTT_protocol_example_without_QoS.svg.png)
(vgl. [7] MQTT)
---
## Weiterführende Informationen

### QoS (Quality of Service)
MQTT bietet 3 QoS Stufen, die im Client eingestellt werden können:
- QoS=0
Jede Nachricht wird genau einmal gesendet, ohne eine Bestätigung zu verlangen
- QoS=1 (Standard)
Jede Nachricht wird mindestens einmal geliefert, der Client erwartet hier eine Bestätigung des Brokers (PUBACK). Bei keiner Bestätigung wird erneut gesendet
- QoS=2
Jede Nachricht wird genau einmal geliefert, dabei wird auf eine 2-Fache Empfangsbestätigung gesetzt

Dabei muss mit jedem anstieg des Levels mit Performance Einbußen gerechnet werden. Diese kommen von den Bestätigungen des Brokers.
Da QoS eine Client Einstellung ist, können Clients mit unterschiedlichen QoS-Stufen senden.
(vgl. [5] Kommunikationsprotokolle)

### Persistent Session (persistente Sitzungen)
Folgend findest du Informationen über persistente Sessions.
![MQTT Persistent Session](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/persistent_session.png)
(vgl. [5] Kommunikationsprotokolle S.38)

### Retained message
Folgend findest du Informationen über retained messages
![MQTT Retained message](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/retained_message.png)
(vgl. [5] Kommunikationsprotokolle S.40)