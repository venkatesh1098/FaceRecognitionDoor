
int LED = 13; // Use the onboard Uno LED
int obstaclePin = 7;  // This is our input pin
int hasObstacle = HIGH;  // HIGH MEANS NO OBSTACLE

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(obstaclePin, INPUT);
  Serial.begin(9600);  
}
void loop() {
  hasObstacle = digitalRead(obstaclePin); //Reads the output of the obstacle sensor from the 7th PIN of the Digital section of the arduino
  Serial.println(hasObstacle);
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
  delay(200);
}






/*int LED = 13; // Use the onboard Uno LED
int isObstaclePin = 7;  // This is our input pin
int isObstacle = HIGH;  // HIGH MEANS NO OBSTACLE
int sensorPin = 0; //analog pin 0

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(isObstaclePin, INPUT);
  Serial.begin(9600);
  
}

void loop() {
  isObstacle = digitalRead(isObstaclePin);
  int val = analogRead(sensorPin);
  Serial.println(val);

  if (isObstacle == LOW)
  {
    //Serial.println("OBSTACLE!!, OBSTACLE!!");
    digitalWrite(LED, HIGH);
    //Serial.println(val);

   // hello();
  }
  else
  {
    //Serial.println("clear");
    digitalWrite(LED, LOW);

    //off();
  }
  delay(400);
}

void hello()
{
Serial.println("HEllo On");
}

void off(){
Serial.println("OFF Chalu");
}
*/
