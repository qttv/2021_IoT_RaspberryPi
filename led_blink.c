#include <wiringPi.h>
#define LED_PIN 7
int main (void)
{
  wiringPiSetup () ;
  pinMode (LED_PIN, OUTPUT) ;
  for (int i=0;;i++)
  {
    digitalWrite (LED_PIN, HIGH) ; delay (50) ;
    digitalWrite (LED_PIN,  LOW) ; delay (50) ;
  }
  return 0 ;
}