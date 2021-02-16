#include<Arduino.h>
int x;
void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 pinMode(13, OUTPUT);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();

  switch (x)
  {
  case 1:
    digitalWrite(13, true);
    break;
  case 2:
    digitalWrite(13, false);
    break;

  default:
    //do nothing
    break;
  }
  x = 0; //reet x as to keep the code dorment
}