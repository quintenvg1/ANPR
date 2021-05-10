int x;
int pos;
#include<Servo.h>

Servo myservo;

void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 pinMode(13, OUTPUT);
 myservo.attach(9);
 pinMode(5, INPUT);
}

void open(){
   for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void close(){
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void loop() {
 //while (!Serial.available());
 x = Serial.readString().toInt();

 if(digitalRead(5)){
        Serial.println("button pressed");
        open();
        delay(2000);
        close();
        //delay(2000);
      }

  switch (x)
  {
  case 1:
    digitalWrite(13, true);
    open();
    Serial.println("opening");
    break;
  case 2:
    digitalWrite(13, false);
    Serial.println("closing");
    close();
    break;

  default:
    //do nothing  
    break;
  }
  x = 0; //reet x as to keep the code dorment

}
