import cv2

path = "images/opencv.png"
image = cv2.imread(path)

print(image)
print(image.shape)

resized_image = cv2.resize(image, (640,480))

cv2.imshow("Original", image)
cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()