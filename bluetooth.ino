/*
 * Bluetooth Module: HC-05
 * 
 * BLUETOOTH ADDRESS: 98D3:51:F5C201
 * UART:9600,0,0
 * NAME:'BLUEY'
 */

#include <SoftwareSerial.h>

SoftwareSerial bluetooth(6, 5); // RX | TX (from arduino pov)

int state = 0;
int laststate = 0;

void setup() {
  bluetooth.begin(9600); // begin bluetooth serial port
  Serial.begin(9600); // begin usb serial port
  pinMode(8, INPUT_PULLUP);
}

void loop() {
  state = digitalRead(8);
  if (state != laststate) {
    if (!state) {
      bluetooth.println("ping");
      Serial.println("yeetus");
    }
  }
  laststate = state;
  delay(100);
}