import cv2

path = "images/opencv.png"
img = cv2.imread(path)

rotated_img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_img_180 = cv2.rotate(img, cv2.ROTATE_180)
rotated_img_90_C = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.ROTATE_180
# cv2.ROTATE_90_CLOCKWISE
# cv2.ROTATE_90_COUNTERCLOCKWISE



cv2.imshow("Image", img)

cv2.imshow("Image 90", rotated_img_90)
cv2.imshow("Image 180", rotated_img_180)
cv2.imshow("Image 90 C", rotated_img_90_C)

cv2.waitKey(0)
cv2.destroyAllWindows()