import cv2

cap=cv2.VideoCapture('output.avi')


if not cap.isOpened():
  print('Camera open failed')
  exit()

while True:
  ret,frame = cap.read()
  if not ret:
    break

  cv2.imshow('frame',frame)
  out.write(frame)

  if cv2.waitKey(10) == 27:
    break

cap.release()
out.release()
cv2.destroyAllWindows()