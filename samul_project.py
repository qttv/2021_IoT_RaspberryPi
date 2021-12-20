import time

import cv2
import RPi.GPIO as GPIO

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
    GPIO.output(segment,GPIO.LOW)

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

  # eyes 가 비어있는 시간 cnt가 10이상이면 불
  # 20 이상이면 부저도
  # 스위치로 cnt 증가를 멈출 수 있다.

try:
  while True:
    ret,img = cap.read()
    face_cascade=cv2.CascadeClassifier('./xml/face.xml')
    eye_cascade=cv2.CascadeClassifier('./xml/eye.xml')

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)

    for(x ,y ,w ,h) in faces:
      #원본 이미지에 얼굴 위치 표시
      cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0), 2)

      #ROI(Region of Interest, 관심영역)
      roi_color = img[y:y+h, x:x+w]
      roi_gray = gray[y:y+h, x:x+w]

      #눈검출
      eyes = eye_cascade.detectMultiScale(roi_gray)

      for(ex, ey, ew, eh) in eyes:
          cv2.rectangle(roi_color, (ex, ey),(ex+ew, ey+ eh), (0, 255, 0), 2)
    #eyes가 없을때를 눈의 길이가 0일때로 조건문을 작성함
    if len(eyes)==0:
        val+=1
        
    print(val)
    #7세그먼트 숫자 표시
    for i in range(len(SEGMENT_PINS)):
        GPIO.output(SEGMENT_PINS[i],Ndata[val][i])    
    time.sleep(1)

    if val==3:#원래 제품은 분 단위이지만, 실습영상 촬영용도로 초로 변경하였습니다.
      GPIO.output(LED_PIN,GPIO.HIGH)  
      time.sleep(1)
      GPIO.output(LED_PIN,GPIO.LOW) 
    
    #부져 껐다 키기
    if val==5:#원래 제품은 분 단위이지만, 실습영상 촬영용도로 초로 변경하였습니다.
      pwm.start(50)
      time.sleep(5)
      pwm.stop()
finally:
    cap.release()
    cv2.destroyAllWindows()
    print(val)    
    GPIO.cleanup()
    print('cleanup and exit')