SEEL4213-01_22231_Group8
- Seak Jian De
- Soh Khai Yang
- Ong Yik Hern

# Remote Patient Monitoring/Alert System
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge&logo=appveyor)](https://www.python.org/) [![Running](https://img.shields.io/badge/running-yes-green.svg?style=for-the-badge&logo=appveyor)]([https://your-project-url.com](http://139.59.254.206/))

# Demo (running)
## URL
http://139.59.254.206/

# Setup

## Libraries Used
```
click==8.1.3
Flask==2.2.2
Flask-MQTT==1.1.1
gunicorn==20.1.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
paho-mqtt==1.6.1
psycopg2-binary==2.9.5
Werkzeug==2.2.2
```
## Run
```
flask --app main run
```

# Big Picture
![Big Picture](https://github.com/jiande-my/SEEL4213-01_22231_Group8/blob/main/static/images/SW_BigPicture.jpg?raw=true)

The edge device, which consists of an ESP82 and an ECG sensor, is used to collect data and send it to a Flask server via MQTT protocol. The Flask server is responsible for receiving and storing the data in a PostgreSQL database, which is hosted on a DigitalOcean server. The Flask server uses this data to generate visualizations and provide real-time updates to the frontend. The visualizations, such as graphs and maps, are generated using the bootstrap, apexchart.js, and leaflet libraries, and are designed to provide insights into the ECG data and to support real-time monitoring of patient health. The Flask application is served using Gunicorn and a reverse proxy, NGINX, is used to manage the incoming traffic to the server.

## Hardware
Arduino

## Communication
In this project, the MQTT client subscribes to a specific topic, which represents the id of the patient. The topic is used to identify the source of the incoming data and to determine where the data should be stored in the database.

When the MQTT client receives a message, the payload of the message is in JSON format, which contains a single key-value pair: "ecg" and its corresponding value. The "ecg" key represents the ECG data collected by the edge device and the sensor, and the value is the actual ECG measurement.

## Database (Postregsql)
### Table 1: Patients

| id	| name	| geolat	| geolong	| heartbeat	| o2_saturation	| bloodpressure |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1	| John	| 40.7128	| 74.0060	| 70	| 96	| 120/80 | 
| 2	| Jane	| 37.7749	| 122.4194	| 72 |	98	| 110/70 |

### Table 2: ECG Data

patient_id	| timestamp	| ecg
| ----------- | ----------- | ----------- |
| 1	| 2022-07-01 10:00:00	| 72.3 |
| 1	| 2022-07-01 10:01:00	| 71.5 |
| 2	| 2022-07-01 10:02:00	| 74.1 |

The two tables are linked through the "patient_id" column in the ECG Data table and the "id" column in the Patients table. The "patient_id" column in the ECG Data table refers to the "id" column in the Patients table and represents the relationship between a patient and their ECG data. This means that the ECG data of each patient can be retrieved by querying the ECG Data table with the corresponding "patient_id".

## Server
Gunicorn and Nginx are popular technologies for deploying and hosting Flask applications on a remote server, such as DigitalOcean. Here are some technical details about the setup:

Gunicorn: Gunicorn is a Python Web Server Gateway Interface (WSGI) HTTP server. It acts as a bridge between your Flask application and a web server, providing workers to handle incoming requests. Gunicorn can handle multiple concurrent requests and is highly scalable, making it a good choice for production-level applications.

Nginx: Nginx is a high-performance web server that can act as a reverse proxy, load balancer, and HTTP cache. When used in conjunction with Gunicorn, Nginx can handle incoming requests and forward them to Gunicorn for processing. Nginx can also handle tasks such as serving static files, compressing responses, and handling SSL certificates, freeing up Gunicorn to focus on running your application.

DigitalOcean: DigitalOcean is a cloud infrastructure provider that offers virtual servers for deploying and hosting applications. By using DigitalOcean, you can easily deploy and manage your Flask application in the cloud, scaling resources as needed.

## Client 
The client side of the project refers to the user interface and the user experience of the system. In this project, the client side is developed using bootstrap and JavaScript libraries like apexcharts.js and leaflet.js.

Bootstrap is a popular front-end framework that provides a responsive and clean design for the user interface. It enables the development of responsive web pages that adjust their layout based on the size of the user's screen.

Apexcharts.js is a JavaScript charting library that allows for the creation of interactive and visually appealing charts and graphs. This library is used to display the data received from the edge device and ECG sensor in the form of graphs and charts.

Leaflet.js is an open-source JavaScript library for creating maps. In this project, it is used to display the geographical location of the patient on a map.

Together, these technologies provide a rich user experience and allow the users to view and interact with the data in a meaningful way. The client-side code receives data from the Flask server and displays it to the user in a visually appealing and interactive format.
