#include <ESP8266WiFi.h>        // Include the Wi-Fi library
#include <WiFiUdp.h>

const char *ssid = "HadiElnemr"; // The name of the Wi-Fi network that will be created
const char *password = "21012101";   // The password required to connect to it, leave blank for an open network

WiFiUDP Udp;
unsigned int localUdpPort = 4210;  // local port to listen on
char incomingPacket[255];  // buffer for incoming packets
char  replyPacket[] = "Hi there! Got the message :-)";  // a reply string to send back

char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1]; //buffer to hold incoming packet,


void setup() {
  // pinMode(D0,OUTPUT);
  pinMode(D1,OUTPUT);
  pinMode(D2,OUTPUT);
  pinMode(D3,OUTPUT);
  Serial.begin(115200);
  delay(10);
  Serial.println('\n');

  WiFi.begin(ssid, password);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(ssid); Serial.println(" ...");

  int i = 0;
  while (WiFi.status() != WL_CONNECTED) { // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  // digitalWrite(D0, LOW);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, LOW);
  analogWrite(D3, 0);
  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer

  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    int n = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    
    if (packetBuffer[0] == 'a'){
      analogWrite(D3, 255); // out of 1023
      Serial.println("a: Up");
    }
    else if (packetBuffer[0] == 'd'){
      analogWrite(D3, 25);
      Serial.println("d: Idle");
    }
    else if (packetBuffer[0] == 'i'){
      analogWrite(D3, 0);
      Serial.println("i: Off");
    }
    Serial.println(packetBuffer);    
  }
  
  delay(10);
 }
