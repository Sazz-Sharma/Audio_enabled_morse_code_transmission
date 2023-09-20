#include <RH_ASK.h>
#ifdef RH_HAVE_HARDWARE_SPI
#include <SPI.h> // Not actually used but needed to compile
#endif
String morse_string;

RH_ASK driver(2000, 4, 2, 5); // ESP8266 or ESP32: do not use pin 11 or 2


void setup()
{
#ifdef RH_HAVE_SERIAL
    Serial.begin(9600);	  // Debugging only
#endif
    if (!driver.init())
#ifdef RH_HAVE_SERIAL
         Serial.println("init failed");
#else
	;
#endif
  pinMode(12, OUTPUT);
}

void loop()
{

    uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];
    uint8_t buflen = sizeof(buf);

    if (driver.recv(buf, &buflen)) // Non-blocking
    {

  String rcv;
  for(int i = 0; i<buflen; i++ ){
      rcv+=(char)buf[i];
  }

  Serial.println(rcv);
  int rcv_len = rcv.length();
  for(int i = 0; i<buflen; i++){
    char current_char = rcv.charAt(i);
    if(current_char == '.'){
      tone(12, 1000);
      delay(100);
      noTone(12);
      delay(100);
    }
    else if(current_char == '-'){
      tone(12, 1000);
      delay(300);
      noTone(12);
      delay(100);
    }
    else if(current_char == '/'){
      noTone(12);
      delay(500);
    }
    else if(current_char == ' '){
      noTone(12);
      delay(300);
    }
  }
    }  
  }
