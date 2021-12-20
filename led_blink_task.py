import RPi.GPIO as GPIO
import time

R = 4
Y = 17
G = 5
GPIO.setmode(GPIO.BCM)  #GPIO.BCM or GPIO.BOARD
GPIO.setup(R,GPIO.OUT) #GPIO.OUT or GPIO.IN
GPIO.setup(Y,GPIO.OUT) #GPIO.OUT or GPIO.IN
GPIO.setup(G,GPIO.OUT) #GPIO.OUT or GPIO.IN

while (True):
  GPIO.output(R,GPIO.HIGH)  # 1 , True , GPIO.HIGH
  print("Red Led On")
  time.sleep(2)
  GPIO.output(R,GPIO.LOW) # 0, False, GPIO.LOW
  print("Red Led Off")
  GPIO.output(Y,GPIO.HIGH)  # 1 , True , GPIO.HIGH
  print("Yellow Led On")
  time.sleep(2)
  GPIO.output(Y,GPIO.LOW) # 0, False, GPIO.LOW
  print("Yellow Led Off")
  GPIO.output(G,GPIO.HIGH)  # 1 , True , GPIO.HIGH
  print("Green Led On")
  time.sleep(2)
  GPIO.output(G,GPIO.LOW) # 0, False, GPIO.LOW
  print("Green Led Off")

GPIO.cleanup()