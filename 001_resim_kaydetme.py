import cv2

img = cv2.imread("images/opencv.png")
cv2.imwrite("images/save_opencv.png", img)
print("[INFO].. DONE !")
