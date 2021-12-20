import RPi.GPIO as GPIO
import time

SWITCH_PIN = 8
GPIO.setmode(GPIO.BCM)  #GPIO.BCM or GPIO.BOARD
GPIO.setup(SWITCH_PIN,GPIO.IN) #GPIO.OUT or GPIO.INf

try: 
  while True:
    val= GPIO.input(SWITCH_PIN)
    print(val)
    time.sleep(0.1)
finally:
  GPIO.cleanup()
  print('cleanup and exit')
