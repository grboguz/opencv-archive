import cv2
import imutils
import requests
import numpy as np

# https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en&pli=1


url = "http://192.168.1.4:8080/shot.jpg"

while True:
    img_respond = requests.get(url)
    img_array = np.array(bytearray(img_respond.content), dtype=np.uint8)
    
    img = cv2.imdecode(img_array, -1)
    # image proseeeing blocks
    img = imutils.resize(img, width = 480, height=360)
    # image proseeeing blocks
    cv2.imshow("Android Camera", img)
    
    if cv2.waitKey(10) == 27: 
        break
    

cv2.destroyAllWindows()