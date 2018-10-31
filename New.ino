//MOTOR CONNECTION
const int motorPinA = 10;// PIN 7 OF L293D 
const int motorPinB = 9;//PIN 2 OF L293D


// PROXIMITY CONNECTION
const int led = 13; //led connection 
const int obstaclePin = 7;// Output of proximity sensor
const int hasObstacle = HIGH;//inital condition of led


void setup(){
    pinMode(led,OUTPUT);
    pinMode(obstaclePin,INPUT);
    Serial.begin(9600);
    pinMode(motorPinA,OUTPUT);
    pinMode(motorPinB,OUTPUT);
    
}

void loop(){
    hasObstacle = digitalRead(obstaclePin);
    Ser
}
