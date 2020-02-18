/*
 * Firmata is a generic protocol for communicating with microcontrollers
 * from software on a host computer. It is intended to work with
 * any host computer software package.
 *
 * To download a host software package, please click on the following link
 * to open the list of Firmata client libraries in your default browser.
 *
 * https://github.com/firmata/arduino#firmata-client-libraries
 */

/* This sketch accepts strings and raw sysex messages and echos them back.
 *
 * This example code is in the public domain.
 */
#include <Firmata.h>

void myCallback(byte command, byte argc, byte *argv) /* @GhostRider - My Callback Function */
{
  digitalWrite(9,HIGH);
  Firmata.sendSysex(command, argc, argv);
}

void setup()
{
  Firmata.setFirmwareVersion(FIRMATA_FIRMWARE_MAJOR_VERSION, FIRMATA_FIRMWARE_MINOR_VERSION);
  Firmata.attach(0x03,myCallback);  /* @GhostRider - Created Own CallBack */
  Firmata.begin(57600);
}

void loop()
{
  while (Firmata.available()) {
    Firmata.processInput();
  }
}
