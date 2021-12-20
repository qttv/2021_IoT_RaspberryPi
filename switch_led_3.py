import RPi.GPIO as GPIO

red = 5
yellow = 6
green = 19
sred = 10
syellow = 9
sgreen = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(sred, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(syellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(sgreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
  while True:
    ron = GPIO.input(sred)
    yon = GPIO.input(syellow)
    gon = GPIO.input(sgreen)
    GPIO.output(red, ron)
    GPIO.output(yellow, yon)
    GPIO.output(green, gon)

finally:
  GPIO.cleanup()
  print('cleanup and exit')
  print('cleanup and exit')
