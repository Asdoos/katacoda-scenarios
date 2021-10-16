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

## Heizungs Client