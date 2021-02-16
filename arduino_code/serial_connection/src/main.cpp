#include <Arduino.h>

int a;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    a = Serial.read(); //trying to read an integer sent from python (1 open gate, 2 close gate)
    if(a == 1){
      digitalWrite(13, true);
    }
    if(a == 2){
      digitalWrite(13, false);
    }
    a = 0;
  }

}