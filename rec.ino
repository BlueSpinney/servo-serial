#include <Servo.h>
Servo servo1;
int servoPin = 9;

int x = 1;
int pos = 0;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 servo1.attach(servoPin);
 
}
void loop() {
 while (!Serial.available()){

 }
 
 
  x = Serial.readString().toInt();
  servo1.write(x);
 
}
