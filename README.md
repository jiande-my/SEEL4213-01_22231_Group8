SEEL4213-01_22231_Group8
- Seak Jian De
- Soh Khai Yang
- Ong Yik Hern

# Remote Patient Monitoring/Alert System

## Problem Statement
The vitality of the pre-hospitalised patients is significantly important to the medical officer to diagnose the clinical event of the patient and provide specific treatment. However, the precise vitality of the patient such as the complete ECG diagram can hardly be sent by the rescue officer to the medical officer in hospital for prior clinical event diagnosis. Hence, a remote ECG monitoring system with cloud server is crucially needed by the medical team to plan and provide the best treatment to the patient before being hospitalized.

## System Architecture
| ![Sensor Architecture](https://github.com/jiande-my/SEEL4213-01_22231_Group8/blob/main/static/images/Slide2.jpg?raw=true) |
|:--:|
| <b>Figure1 - Sensor Device Data Transmission</b>|


| ![Cloud Architecture](https://github.com/jiande-my/SEEL4213-01_22231_Group8/blob/main/static/images/Slide4.jpg?raw=true) |
|:--:|
| <b>Figure2 - Cloud Platform Architecture</b>|

## Sensor
In the remote ECG monitoring system, an AD8232 sensor is used to measure the electrical activity of the heart. This electrical activity can be charted as an ECG or Electrocardiogram and output as an analog reading. ECGs can be extremely noisy, the AD8232 Single Lead Heart Rate Monitor acts as an op amp to help obtain a clear signal from the PR and QT Intervals easily.

## Cloud Platform
- Django Web App deplay on Azure
- Database that will be use is PostreqSQL

## Dashboard
An interactive dashboard for remote ECG monitoring system will be designed by using Grafana to visualize results from multiple data sources simultaneously. 
