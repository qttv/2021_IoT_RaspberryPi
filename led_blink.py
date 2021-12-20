import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)  #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN,GPIO.OUT) #GPIO.OUT or GPIO.IN

while (True):
  GPIO.output(LED_PIN,GPIO.HIGH)  # 1 , True , GPIO.HIGH
  #print("led on")
  time.sleep(0.05)
  GPIO.output(LED_PIN,GPIO.LOW) # 0, False, GPIO.LOW
  #print("led off")
  time.sleep(0.05)

GPIO.cleanup()