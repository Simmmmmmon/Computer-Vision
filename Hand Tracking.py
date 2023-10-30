import cv2
import mediapipe as mp
import time
import numpy as np

Ptime = 0
Ctime = 0
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                cv2.circle(img, (cx,cy), 15, (200,0,200),cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    Ctime = time.time()
    fps = 1 / (Ctime-Ptime)
    PTime = Ctime

    cv2.putText(img, str(int(fps)),(30,70), cv2.FONT_HERSHEY_PLAIN,4,(255,0,255),4)


    cv2.imshow("Image", img)
    cv2.waitKey(1)


