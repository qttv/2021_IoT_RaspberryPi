import RPi.GPIO as GPIO
import time

LED_PIN = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0)  # duty cycle

def changePWM(cycle, delay):
  pwm.ChangeDutyCycle(cycle)
  time.sleep( delay)

try:
  while (True):
    for j in range(0, 101, 10):
      changePWM(j, .1)
    for j in range(100, -1, -10):
      changePWM(j, .1)

finally:
  pwm.stop()
  GPIO.cleanup()
