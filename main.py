from flask import Flask, render_template
from flask_mqtt import Mqtt
import database as db

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
    patients = db.get_patient_detail()
    return render_template('dashboard.html',patients=patients)

@app.route("/<id>")
def devices(id):
    patients = db.get_patient_detail()
    detail = db.get_single_patient_detail(id)
    ecg, ecg_time = db.get_ecg_data(id)
    print(ecg_time)
    return render_template('devices.html', id=id, detail=detail, patients=patients, ecg=ecg, ecg_time=ecg_time)
