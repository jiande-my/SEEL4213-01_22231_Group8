from flask import Flask, render_template
from flask_mqtt import Mqtt

app = Flask(__name__, static_folder='assets')

app.config['MQTT_BROKER_URL'] = '139.59.254.206'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'jiande'  # Set this item when you need to verify username and password
app.config['MQTT_PASSWORD'] = 'utm123'  # Set this item when you need to verify username and password
app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
topic = '#'

mqtt_client = Mqtt(app)

@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe(topic) # subscribe topic
   else:
       print('Bad connection. Code:', rc)

@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print('Received message on topic: {topic} with payload: {payload}'.format(**data))

@app.route("/")
def dashboard():
    data = [31, 40, 28, 51, 42, 82, 56]
    devices = [1, 2, 3]
    return render_template('dashboard.html',devices=devices)

@app.route("/devices/<id>")
def devices(id):
    data = [31, 40, 28, 51, 42, 82, 56]
    devices = [1, 2, 3]
    return render_template('devices.html',devices=devices,data=data,id=id)
