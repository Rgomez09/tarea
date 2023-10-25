#include <Stepper.h>
int sepsPerRevolution = 2048;
int motSpeed = 10;
Stepper myStepper(sepsPerRevolution,8,10,9,11);

void setup() 
{
  myStepper.setSpeed(motSpeed);
}

void loop() 
{
  myStepper.step(sepsPerRevolution);
}
