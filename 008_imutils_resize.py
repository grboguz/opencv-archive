import cv2
import imutils


path = "images/opencv.png"
img = cv2.imread(path)
#print(img)


for width in (500, 300, 100):
    resized_img = imutils.resize(img, width=width)
    cv2.imshow("%d" % (width), resized_img)


cv2.waitKey(0)
cv2.destroyAllWindows()