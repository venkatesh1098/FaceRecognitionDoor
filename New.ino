//MOTOR CONNECTION
const int motorPinA = 10;// PIN 7 OF L293D 
const int motorPinB = 9;//PIN 2 OF L293D

// PROXIMITY CONNECTION
const int led = 13; //led connection 
const int obstaclePin = 7;// Output of proximity sensor
const int hasObstacle = HIGH;//inital condition of led

//Data comming from python
int data=1;

void setup(){
    pinMode(led,OUTPUT);
    pinMode(obstaclePin,INPUT);
    Serial.begin(9600);
    pinMode(motorPinA,OUTPUT);
    pinMode(motorPinB,OUTPUT);

}

void loop(){
  Serial.println(data);
  data=data+1;
  //while(Serial.available()){
        //data=Serial.read();
        //Serial.println(data+1);
        if (data==5){
          data=1;
        }
        
        if (data == 1)
            {
              //UnLocks the door by clockwise direction of motor
                digitalWrite(motorPinA, HIGH);
                digitalWrite(motorPinB, LOW);
                Serial.print("Lock");
                delay(800); 
                digitalWrite(motorPinA, LOW);
                digitalWrite(motorPinB, LOW);
                delay(1000);
                digitalWrite(motorPinA, LOW);
                digitalWrite(motorPinB, HIGH);
                delay(800); data=data+1;
            
          }
        else{
                // locks the door by rotating anticlockwise
                digitalWrite(motorPinA, LOW);
                digitalWrite(motorPinB, LOW);
                delay(500); 
                digitalWrite(motorPinA, LOW);
                digitalWrite(motorPinB, LOW);
                delay(2000);    
                digitalWrite(motorPinA, LOW);
                digitalWrite(motorPinB, LOW);  
        }
 // }
}

