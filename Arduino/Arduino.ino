int led1 = 0;
int led2 = 0;
int led3 = 0;

#define LED1 49
#define LED2 52
#define LED3 53


char statu;
void setup()
{
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
  statu = 255;
  Serial.begin(9600);
  attachInterrupt(0, LD1, RISING);
  attachInterrupt(1, LD2, RISING);
  attachInterrupt(2, LD3, RISING);
}

void LD1()
{
  int estado1 = digitalRead(LED1);
  if (estado1 == 1)
  {
    digitalWrite(LED1, 0);
    led1 = 0;
  } else
  {
    digitalWrite(LED1, 1);
    led1 = 1;
  }
  statu == 255;
}

void LD2()
{
  int estado2 = digitalRead(LED2);
  if (estado2 == 1)
  {
    digitalWrite(LED2, 0);
    led2 = 0;
  } else
  {
    digitalWrite(LED2, 1);
    led2 = 1;
  }
  statu == 255;
}

void LD3()
{
  int estado3 = digitalRead(LED3);
  if (estado3 == 1)
  {
    digitalWrite(LED3, 0);
    led3 = 0;
  } else
  {
    digitalWrite(LED3, 1);
    led3 = 1;
  }
  statu == 255;
}

void serialEvent()
{
  if (Serial.available() > 0)
  {
    Serial.write(led1);
    Serial.write(led2);
    Serial.write(led3);
    statu = Serial.read();
  }

  if (statu == '6')
  {
    digitalWrite(LED1, 0);  // turn the LED on (HIGH is the voltage level)
    led1 = 0;
  }
  else if (statu == '1')
  {
    digitalWrite(LED1, 1);
    led1 = 1;
  }
  else if (statu == '2')
  {
    digitalWrite(LED2, 0);
    led2 = 0;
  }
  else if (statu == '3')
  {
    digitalWrite(LED2, 1);
    led2 = 1;
  }
  else if (statu == '4')
  {
    digitalWrite(LED3, 0);
    led3 = 0;
  }
  else if (statu == '5')
  {
    digitalWrite(LED3, 1);
    led3 = 1;
  }
}

void loop() {

}
