import cv2

img = cv2.imread("images/opencv.png")
print(img.shape)

# x axis - parameter: 0
x_flipped = cv2.flip(img, 0)

# y axis - parameter: 1
y_flipped = cv2.flip(img, 1)

# x-y axis - parameter: -1
xy_flipped = cv2.flip(img, -1)



cv2.imshow("Image", img)

cv2.imshow("X", x_flipped)
cv2.imshow("Y", y_flipped)
cv2.imshow("XY", xy_flipped)


cv2.waitKey(0)
cv2.destroyAllWindows()