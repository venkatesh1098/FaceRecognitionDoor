//MOTOR CONNECTION
const int motorPinA = 10;// PIN 7 OF L293D 
const int motorPinB = 9;//PIN 2 OF L293D

// PROXIMITY CONNECTION
const int led = 13; //led connection 
const int obstaclePin = 7;// Output of proximity sensor
const int hasObstacle = HIGH;//inital condition of led

//Data comming from python
int data;

void setup(){
    pinMode(led,OUTPUT);
    pinMode(obstaclePin,INPUT);
    Serial.begin(9600);
    pinMode(motorPinA,OUTPUT);
    pinMode(motorPinB,OUTPUT);
    
}

void loop(){
    hasObstacle = digitalRead(obstaclePin);
    Serial.println(hasObstacle);
    while(Serial.available()){
        data=Serial.read();
        if (data == 1)
            {
              //Locks the door by clockwise direction of motor
                digitalWrite(motorPin3, HIGH);
                digitalWrite(motorPin4, LOW);
                delay(2000); 
                //This code will turn Motor B counter-clockwise for 2 sec.
                digitalWrite(motorPin3, LOW);
                digitalWrite(motorPin4, HIGH);
                delay(500);    
                digitalWrite(motorPin3, LOW);
                digitalWrite(motorPin4, LOW);  
            }
        else
            {
                // Unlocks the door by rotating anticlockwise
                digitalWrite(motorPin3, HIGH);
                digitalWrite(motorPin4, LOW);
                delay(500); 
                digitalWrite(motorPin3, LOW);
                digitalWrite(motorPin4, HIGH);
                delay(2000);    
                digitalWrite(motorPin3, LOW);
                digitalWrite(motorPin4, LOW);  
        }
    }




    if (hasObstacle == LOW) //LOW means something is ahead, so illuminates the 13th Port connected LED
    {
    // Serial.println("Stop something is ahead!!");
        digitalWrite(LED, HIGH);//Illuminates the 13th Port LED
    }
    else
    {
    //Serial.println("Path is clear");
        digitalWrite(LED, LOW);
    }
    delay(1500);
}
}
