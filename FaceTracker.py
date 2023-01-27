import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

pTime, cTime = 0

while True:
    success, img = cap.read()
    
    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'fps: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)