import RPi.GPIO as GPIO
import time

BuzPin=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzPin, GPIO.OUT)

#        도, 레, 미, 파, 솔, 라, 시
melody=[262,294,330,349,392,440,494]
music1=[392,392,440,440,392,392]
music2=[392,392,330,330]
music3=[392,330,294,330]


pwm = GPIO.PWM(BuzPin,392)
pwm.start(10)

for i in music1:
  pwm.ChangeFrequency(i)
  time.sleep(0.5)
  pwm.ChangeFrequency(10)
  time.sleep(0.1)
pwm.ChangeFrequency(330)
time.sleep(1)
pwm.ChangeFrequency(10)
time.sleep(0.1)

for i in music2:
  pwm.ChangeFrequency(i)
  time.sleep(0.5)
  pwm.ChangeFrequency(10)
  time.sleep(0.1)
pwm.ChangeFrequency(294)
time.sleep(1)
pwm.ChangeFrequency(10)
time.sleep(1.2)

for i in music1:
  pwm.ChangeFrequency(i)
  time.sleep(0.5)
  pwm.ChangeFrequency(10)
  time.sleep(0.1)
pwm.ChangeFrequency(330)
time.sleep(1)
pwm.ChangeFrequency(10)
time.sleep(0.1)

for i in music3:
  pwm.ChangeFrequency(i)
  time.sleep(0.5)
  pwm.ChangeFrequency(10)
  time.sleep(0.1)
pwm.ChangeFrequency(262)
time.sleep(1)
pwm.ChangeFrequency(10)
time.sleep(0.1)