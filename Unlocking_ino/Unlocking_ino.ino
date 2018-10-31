//L293D
//Motor B

const int motorPin3  = 10; // Pin  7 of L293
const int motorPin4  = 9;  // Pin  2 of L293

//This will run only one time.

void setup(){
    //Set pins as outputs
    pinMode(motorPin3, OUTPUT);
    pinMode(motorPin4, OUTPUT);
}





void loop(){

//while (Serial.available()){
//  data = Serial.read();
//}
if (data == 1)
{  //Locks the door by clockwise direction of motor
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
else{
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


