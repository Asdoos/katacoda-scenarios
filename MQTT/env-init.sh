mkdir -p /etc/mosquitto/conf.d/
curl -L https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/files/mosquitto.conf > /etc/mosquitto/conf.d/mosquitto.conf

mkdir -p /scripts/
curl -L https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/scripts/fenster.py > /scripts/fenster.py
curl -L https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/scripts/heizung.py > /scripts/heizung.py
curl -L https://raw.githubusercontent.com/Asdoos/katacoda-scenarios/main/MQTT/assets/scripts/requirements.txt > /scripts/requirements.txt

sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.9
cd /scripts/
pip install -r requirements.txt