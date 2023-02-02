#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.

const char* ssid = "WiFi_Capstone";
const char* password = "Password";
const char* mqtt_server = "139.59.254.206";
const char* mqtt_username = "jiande";
const char* mqtt_password = "utm123";
const char* mqtt_topic = "ecg001";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE	(50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

int data[349] = {336, 324, 321, 348, 376, 392, 403, 417, 422, 414, 423, 440, 
              442, 438, 448, 460, 459, 454, 465, 478, 474, 469, 482, 493, 
              484, 480, 490, 498, 488, 486, 494, 488, 474, 474, 482, 477, 
              466, 470, 481, 481, 478, 489, 502, 499, 495, 506, 513, 502, 
              495, 504, 511, 507, 509, 520, 522, 518, 523, 540, 541, 531, 
              536, 546, 541, 531, 538, 547, 541, 535, 543, 547, 535, 523, 
              533, 538, 528, 519, 528, 532, 521, 519, 532, 535, 532, 537, 
              545, 535, 532, 560, 588, 582, 568, 566, 562, 552, 537, 542, 
              538, 517, 502, 510, 514, 506, 506, 512, 507, 488, 474, 498, 
              582, 763, 1024, 1024, 1024, 1024, 877, 548, 409, 379, 377, 
              376, 396, 436, 459, 453, 447, 459, 462, 457, 461, 474, 475, 
              469, 471, 481, 480, 474, 481, 494, 487, 476, 485, 495, 484, 
              474, 478, 481, 466, 456, 460, 459, 444, 437, 440, 440, 430, 
              437, 451, 451, 445, 450, 465, 461, 448, 451, 457, 448, 440, 
              449, 458, 449, 446, 456, 461, 454, 452, 464, 466, 456, 457, 
              464, 460, 449, 449, 456, 447, 433, 432, 438, 430, 415, 420,
              427, 417, 410, 415, 415, 402, 397, 405, 405, 397, 400, 415, 
              417, 404, 405, 427, 440, 442, 450, 451, 430, 406, 411, 415, 
              399, 378, 374, 369, 357, 356, 367, 368, 356, 353, 349, 331, 
              348, 457, 682, 978, 1024, 1024, 999, 613, 313, 258, 243, 213,
              217, 254, 284, 291, 294, 303, 302, 297, 306, 317, 310, 304,
              314, 324, 316, 312, 326, 331, 319, 316, 329, 330, 320, 321, 
              329, 328, 317, 317, 322, 312, 296, 296, 302, 291, 278, 286, 
              296, 293, 290, 303, 314, 306, 303, 314, 314, 304, 305, 315, 
              316, 307, 310, 325, 321, 316, 320, 330, 326, 318, 326, 332, 
              325, 318, 326, 332, 325, 318, 322, 327, 316, 312, 321, 321, 
              308, 304, 314, 312, 301, 300, 308, 306, 295, 296, 306, 303, 
              295, 307, 317, 306, 302, 331, 356, 350, 341, 342, 332, 316, 
              310, 317, 306, 282, 270, 276, 272, 264, 273, 282, 276, 262, 
              248, 248};

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str(), mqtt_username, mqtt_password)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish(mqtt_topic, "hello world");
      // ... and resubscribe
      client.subscribe("/Fan");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  Serial.begin(9600); //initialize the serial communication
  pinMode(14, INPUT); //setup for leads off detection LO +
  pinMode(12, INPUT); //setup for leads off detection LO -
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  for (int i = 0; i < 349; i++) {
    sprintf(msg, "{\"v4\": %d.01, \"mlii\": 0.33}", data[i]);

    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish(mqtt_topic, msg);

    delay(3);     //Wait for a bit to keep serial data from saturating
  }
}
