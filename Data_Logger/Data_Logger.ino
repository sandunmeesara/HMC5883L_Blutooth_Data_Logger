#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>
#include <SoftwareSerial.h>

// Define the pins for SoftwareSerial
SoftwareSerial BTSerial(10, 11); // RX, TX

Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);

void setup() {
  Serial.begin(9600);  // Serial communication for debugging
  BTSerial.begin(9600); // Serial communication for Bluetooth module

  if (!mag.begin()) {
    Serial.println("HMC5883L not detected. Check your wiring!");
    while (1);
  }
}

void loop() {
  sensors_event_t event;
  mag.getEvent(&event);

  // Calculate heading
  float heading = atan2(event.magnetic.y, event.magnetic.x);
  if (heading < 0) {
    heading += 2 * PI;
  }
  float headingDegrees = heading * 180 / M_PI;

  // Calculate magnitude
  float magnitude = sqrt(event.magnetic.x * event.magnetic.x +
                         event.magnetic.y * event.magnetic.y +
                         event.magnetic.z * event.magnetic.z);

  // Send data via Bluetooth
  BTSerial.print("X: "); BTSerial.print(event.magnetic.x);BTSerial.print(",");
  BTSerial.print(" Y: "); BTSerial.print(event.magnetic.y);BTSerial.print(",");
  BTSerial.print(" Z: "); BTSerial.print(event.magnetic.z);BTSerial.print(",");
  BTSerial.print(" Magnitude: "); BTSerial.print(magnitude);BTSerial.print(",");
  BTSerial.print(" Heading: "); BTSerial.println(headingDegrees);

  delay(1000); // Delay to avoid spamming data
}
