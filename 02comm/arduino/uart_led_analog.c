#define LED 13
char cmd;
int val;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
}

void loop() {
  if(Serial.available()){
    cmd = Serial.read();
    if(cmd =='1'){
      digitalWrite(LED, HIGH); 
    }else if(cmd == '0'){
      digitalWrite(LED, LOW);
    }
  }
  val = analogRead(0);
  Serial.println(val);  
}