import cv2
import RPi.GPIO as GPIO
import time
cap=cv2.VideoCapture(0)
#BUZZER의 pin 설정
BUZZER_PIN = 26
LED_PIN=13
# GPIO 7개 pin 번호 설정
SEGMENT_PINS=[21,20,5,6,7,24,23]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)
GPIO.setup(LED_PIN,GPIO.OUT)

for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.setup(segment,GPIO.LOW)

pwm = GPIO.PWM(BUZZER_PIN,262)

Ndata = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9
val = 0

if not cap.isOpened():
  print('Camera open failed')
  exit()

ret,img = cap.read()
face_cascade=cv2.CascadeClassifier('./xml/face.xml')
eye_cascade=cv2.CascadeClassifier('./xml/eye.xml')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)
eyes=eye_cascade.detectMultiScale(gray,1.3,5)

  # eyes 가 비어있는 시간 cnt가 10이상이면 불
  # 20 이상이면 부저도
  # 스위치로 cnt 증가를 멈출 수 있다.


try:
  while True:
      #버튼으로 시간 조작
      if len(eyes)==0:
          val+=1
          break
      print(val)
      #7세그먼트 숫자 표시
      for i in range(len(SEGMENT_PINS)):
          GPIO.output(SEGMENT_PINS[i],Ndata[val][i])    
      time.sleep(1)
  
      if val==180:
        GPIO.output(LED_PIN,GPIO.HIGH)  
        time.sleep(1)
        GPIO.output(LED_PIN,GPIO.LOW) 
      #부져 껐다 키기
      if val==300:
        pwm.start(50)
        time.sleep(5)
        pwm.stop()
finally:
  print(val)
  GPIO.cleanup()
  print('cleanup and exit')
      


cap.release()
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()