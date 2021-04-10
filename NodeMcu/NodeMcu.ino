#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#include <DHT.h>        // importa la Librerias DHT
#include <DHT_U.h>
int SENSOR = 5;            // pin DATA de DHT22 a pin digital 2
DHT dht(SENSOR, DHT11);        // creacion del objeto, cambiar segundo parametro

#include <Thread.h>
#include <ThreadController.h>

Thread hiloDHT = Thread();

#define LED 2

const char* ssid     = "Wisper";
const char* password = "Wispergt2016*";
String dataString = "";


WiFiServer servidorTCP(8266);
WiFiClient clienteTCP;

ThreadController controladorHilos = ThreadController();

void setup() {

  //pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  dht.begin();            // inicializacion de sensor
  delay(100);

  //Serial.print("Conectandose a: ");
  //Serial.println(ssid);

  WiFi.begin(ssid, password);  //Intentamos conectarnos a la red Wifi

  while (WiFi.status() != WL_CONNECTED)
  { //Esperamos hasta que se conecte.
    delay(200);
  }

  //Serial.print ("Conectado, IP: ");
  //Serial.println (WiFi.localIP());

  servidorTCP.begin();

  hiloDHT.onRun(leeDHT);
  hiloDHT.setInterval(1000);
}

void loop()
{
  if (!clienteTCP.connected())
  {
    // try to connect to a new client
    clienteTCP = servidorTCP.available();
    if (clienteTCP.connected())
    {
      //Serial.println("Cliente conectado");
      controladorHilos.add(&hiloDHT);
    }
  } else
  {
    // read data from the connected client
    if (clienteTCP.available() > 0)
    {
      char dato = (char)clienteTCP.read();
      Serial.write(dato);
    }
  }
  controladorHilos.run();
}

void leeDHT()
{
  int led1 = 2;
  int led2 = 2;
  int led3 = 2;
  float TEMP = dht.readTemperature();
  float HUM = dht.readHumidity();
  String valor1 = "";
  String valor2 = "";
  String valor3 = "";
  if (Serial.available() > 0)
  {
    led1 = Serial.read();
    led2 = Serial.read();
    led3 = Serial.read();
    Serial.write('0');
  }

  if (led1 == 0)
  {
    valor1 = "OFF";
  }
  else if (led1 == 1)
  {
    valor1 = "ON";
  }
  else
  {
    valor1 = "Away";
  }
  if (led2 == 0)
  {
    valor2 = "OFF";
  }
  else if (led2 == 1)
  {
    valor2 = "ON";
  }
  else
  {
    valor2 = "Away";
  }
  if (led3 == 0)
  {
    valor3 = "OFF";
  }
  else if (led3 == 1)
  {
    valor3 = "ON";
  }
  else
  {
    valor3 = "Away";
  }

  String datos = "B1 ";
  datos += valor1;
  datos += "\nB2 ";
  datos += valor2;
  datos += "\nB3 ";
  datos += valor3;
  datos += "\nT ";
  datos += TEMP;
  datos += "\nH ";
  datos += HUM;
  datos += "\n";
  //Serial.print(datos);
  clienteTCP.print(datos); // enviamos los datos por el socket

}
