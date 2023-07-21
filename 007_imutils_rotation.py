import cv2
import imutils


path = "images/opencv.png"
img = cv2.imread(path)
#print(img)


for angle in range(0,360,90):
    rotated_img = imutils.rotate(img, angle=angle)
    cv2.imshow("%d" % (angle), rotated_img)


cv2.waitKey(0)

cv2.destroyAllWindows()