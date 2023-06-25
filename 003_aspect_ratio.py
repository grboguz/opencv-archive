import cv2

path = "images/opencv.png"
img = cv2.imread(path)

print(img.shape)
print("Height: ", img.shape[0])
print("Width: ", img.shape[1])
print("Channel: ", img.shape[2])

new_width = 350
old_width = img.shape[1]

ratio = new_width/old_width

dimension = (new_width, int(img.shape[0]*ratio))
resized_image = cv2.resize(img, dimension)
print(resized_image.shape)

cv2.imshow("Original", img)
cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()