import cv2

cap=cv2.VideoCapture(0)


if not cap.isOpened():
  print('Camera open failed')
  exit()

while True:
  ret,frame = cap.read()
  if not ret:
    break

  cv2.imshow('frame',frame)
  img2 = cv2.resize(frame,(600,400))
  gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
  cv2.imshow('gray',gray)
  edge=cv2.Canny(frame,100,150)
  cv2.imshow('edge',edge)

  if cv2.waitKey(10) == 27:
    break

cap.release()
out.release()
cv2.destroyAllWindows()