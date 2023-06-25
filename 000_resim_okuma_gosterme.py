import cv2

image = cv2.imread("images/opencv.png")
print(image.shape)

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
