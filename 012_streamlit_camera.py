import cv2
import numpy as np
import streamlit as st

# streamlit run test.py
# python -m streamlit run test.py

path = "videos\\test_1.mp4"
cap = cv2.VideoCapture(path)

st.title("Video - OpenCV")

place_holder = st.empty()
button = st.button("Stop")

while cap.isOpened() and not button:
    ret, frame = cap.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    place_holder.image(frame, channels="RGB")
    
    if cv2.waitKey(30) & 0xFF ==ord("q") or button:
        break
    
cap.release()
cv2.destroyAllWindows()