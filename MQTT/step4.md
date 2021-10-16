Nun sendet unser "Fenstersensor" jede Minute zufällig ein "ich bin offen" oder "ich bin geschlossen" an den Broker.
Unsere Heizung weiß davon noch nichts und das möchten wir nun ändern.
Dafür wird der Begriff der Subscription eingeführt.

## Subscription
Die zweite Funktion eines MQTT Clients, neben dem Publishen von Werten, ist das subscriben, also abonnieren, von Ausgewählten Werten.
Hier kommen erneut die Topics ins spiel. Der Client abonniert ein bestimmtes Thema und gibt dies dem Broker bekannt.


![MQTT Subscription](https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/images/subscribe_flow.gif)