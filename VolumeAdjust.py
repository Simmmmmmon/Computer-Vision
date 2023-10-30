import cv2
import time
import HandTrackingModule as HTM
import numpy as np

wCam, hCam = 1050, 500


Cam = cv2.VideoCapture(0)
Cam.set(3, wCam)
Cam.set(4, hCam)

frame_count = 0
start_time = time.time()

Detector = HTM.HandDetector()

while True :
    success, Img = Cam.read()
    Detector.findHands(Img)
    List = HTM.

    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        fps = int(frame_count / elapsed_time)
    else:
        fps = 0

    cv2.putText(Img, str(fps), (20, 50), cv2.FONT_HERSHEY_SIMPLEX,2, (50, 255, 0),2)
    frame_count += 1

    cv2.imshow("Front Camera", Img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
