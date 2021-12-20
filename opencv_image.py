import cv2

img = cv2.imread('jessieware.jpg')
img2 = cv2.resize(img,(600,400))

cv2.imshow('collection1.jpg-1280',img2)

cv2.waitKey(0)

cv2.destroyAllWindows()