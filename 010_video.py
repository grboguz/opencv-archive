import cv2
import numpy as np


path = "videos\\test_1.mp4"
cap = cv2.VideoCapture(path) # 0 --> webcam

ret, frame = cap.read()
print(frame.shape)

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    cv2.imshow("Test", frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
    
    """
    key = cv2.waitKey(100)
    if key == 27:
        break
    """

cap.release()
cv2.destroyAllWindows()