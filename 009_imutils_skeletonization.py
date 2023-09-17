import cv2
import imutils 


path = "images\\text.png"
img = cv2.imread(path)
# print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)

skeleton = imutils.skeletonize(gray, size=(5,5))

cv2.imshow("Test", img)
cv2.imshow("Test 1", gray)
cv2.imshow("Test 2", skeleton)

cv2.waitKey(0)
cv2.destroyAllWindows()