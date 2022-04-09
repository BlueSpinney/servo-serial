#include <Servo.h>
Servo servo1;
Servo servo2;
int servoPin = 9;
int servo2Pin = 10;

int x = 1;
int pos = 0;
int count = 0;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 servo1.attach(servoPin);
 servo2.attach(servo2Pin);
 
}
void loop() {
 while (!Serial.available()){

 }
 
 
  x = Serial.readString().toInt();
  Serial.println(x);
  if (count == 0){
    Serial.println("sending to s1");
    servo1.write(x);
    count = 1;
  }
  else if (count ==1){
    Serial.println("sending to s2");
    servo2.write(x);
    count = 0;
  }
}
