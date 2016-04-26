int relay1 = 7;
int relay2 = 8;
int led = 13;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(relay2,OUTPUT);
  pinMode(relay1,OUTPUT);
  pinMode(led,OUTPUT);
  digitalWrite(led,HIGH);
  delay(500);
  digitalWrite(led,LOW);
  delay(500);
   digitalWrite(led,HIGH);
   digitalWrite(relay2,LOW);
   digitalWrite(relay1,LOW);
  while(!Serial.available());
  Serial.read();
  digitalWrite(led,LOW);
  
}

void loop() {
  while(!Serial.available());
  while(Serial.available())
    Serial.read();

  digitalWrite(led,HIGH);
  digitalWrite(relay2,HIGH);
  digitalWrite(relay1,HIGH);
  delay(20000);
  digitalWrite(led,LOW);
  digitalWrite(relay2,LOW);
  digitalWrite(relay1,LOW);
 
}
