import cv2
import imutils


path = "images/opencv.png"
img = cv2.imread(path)
#print(img)

translated_img = imutils.translate(img, 50, 75)

cv2.imshow("Test", img)
cv2.waitKey(0)

cv2.imshow("Test", translated_img)
cv2.waitKey(0)

cv2.destroyAllWindows()