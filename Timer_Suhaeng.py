import time
import RPi.GPIO as g

# 4 digit fnd 출력 숫자
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9
  
buz=21                        #피에조 부저 핀
switch2=26                    #초기화 스위치 핀
led = 2                       #LED 핀
switch = 4                    #10초 추가 스위치 핀
signal = [5,6,7,8,9,10,11]    #4 digit fnd 신호 핀
digitpin = [12,13,14,15]      #4 digit fnd 자리수 핀 

g.setmode(g.BCM)                                       #GPIO 설정
g.setup(led, g.OUT)                                    #LED 설정
g.setup(buz, g.OUT)                                    #부저 설정
g.setup(switch, g.IN, pull_up_down=g.PUD_UP)           #초기화 스위치 핀
g.setup(switch2, g.IN, pull_up_down=g.PUD_UP)          #10초 추가 스위치 핀

for segment in signal:                                 #4 digit fnd 출력 설정
  g.setup(segment,g.OUT)
  g.output(segment,g.LOW)

for digit in digitpin:
  g.setup(digit,g.OUT)
  g.output(digit,g.HIGH)



def display(digit,tar):                                    #4 digit fnd 자리수(digit)에 원하는 숫자(tar) 출력

  for i in range(len(digitpin)):
    if i +1==digit:
      g.output(digitpin[i],g.LOW)
    else:
      g.output(digitpin[i],g.HIGH)
  
  for i in range(len(signal)):    
    g.output(signal[i],data[tar][i])

  time.sleep(0.001)

cnt=0       #화면 출력 숫자
cnt=int(cnt) # 정수형으로 바꿈
val=0       #스위치 입력값

start = time.perf_counter() #프로그램 시작 시간
predur=0  #방금 전까지의 프로그램이 돌아간 시간
end=0     #현재 시간
dur=0     #지금까지의 프로그램이 돌아간 시간
val2=0    #초기화 스위치 입력값
g.output(led, g.LOW) #LED 끄고 시작
pwm = g.PWM(buz,1)  #피에조 부저 주파수 설정
pwm.start(10)

try:
  while True:          # 반복
    if cnt==0:         # 남은 시간이 0이 되면 불 켬
      g.output(led,g.HIGH)
    else:              # 아닌 경우 끔
      g.output(led,g.LOW)
    if dur!=0:         #처음이 아닌 경우 predur에 dur 대입
      predur=dur
    end = time.perf_counter() #end에 현재 시간 입력
    dur=end-start             #dur 새로 입력
    #print(dur)
    if  (int(dur) - int(predur))==1 and cnt>=1 :   #앞 자리수가 하나 오를 때 숫자 증가
      cnt=cnt-1
    a=cnt//1000                 #자릿수 대로 출력
    b=(cnt//100)%10
    c=(cnt//10)%10
    d=(cnt%10)
    display(1,a)
    display(2,b)
    display(3,c)
    display(4,d)
    prev2=val2               # 전 스위치2 값
    prev=val                 # 전 스위치1 값
    val = g.input(switch)   # 스위치 값 새로 입력
    val2=g.input(switch2)
    #print(val2)
    if prev2==1 and val2==0:    #초기화 스위치가 눌렸을 때 초기화함
      cnt=0
    #print(val)
    if prev==1 and val ==0:     # 10초 추가 스위치가 눌렸을 때 추가
      cnt+=10
    if val2==0:                 #스위치2가 눌렸을 때 소리 남
      pwm.ChangeFrequency(494)
    if val2==1:                 #아닌 경우 수리 끔
      pwm.ChangeFrequency(1) 
finally:
  g.cleanup()
  print('cleanup and exit')