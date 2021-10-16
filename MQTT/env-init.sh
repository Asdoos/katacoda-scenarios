mkdir -p /etc/mosquitto/conf.d/
curl -L https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/files/mosquitto.conf > /etc/mosquitto/conf.d/mosquitto.conf

mkdir -p /scripts/fenster/
curl -L https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/scripts/fenster/main.py > /scripts/fenster/main.py

sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.9