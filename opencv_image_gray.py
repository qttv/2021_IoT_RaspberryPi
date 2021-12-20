import cv2

img = cv2.imread('jessieware.jpg')
img2 = cv2.resize(img,(600,400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('jessieware',img2)
cv2.imshow('jessieware_GRAY',gray)


while True:
  if cv2.waitKey() == ord('q'):
    break

cv2.imwrite('jessieware_GRAY.jpg',gray)
cv2.destroyAllWindows()