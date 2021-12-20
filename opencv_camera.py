import cv2

cap=cv2.VideoCapture(0)


if not cap.isOpened():
  print('Camera open failed')
  exit()

ret,frame = cap.read()
cv2.imwrite('output.jpg',frame)

cap.release()
cv2.destroyAllWindows()