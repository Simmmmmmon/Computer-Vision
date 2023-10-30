import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
frame_count = 0
start_time = time.time()
while True :
    success, img = cap.read()
    ImgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    Results = pose.process(ImgRGB)
    print(Results.pose_landmarks)
    if Results.pose_landmarks :
        mpDraw.draw_landmarks(img, Results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(Results.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id, lm)
            cx, cy  = int(lm.x*w), int(lm.y*h)
            cv2.circle(img,(cx,cy), 8, (57,200,63), cv2.FILLED)


    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        fps = int(frame_count / elapsed_time)
    else:
        fps = 0

    cv2.putText(img, str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    frame_count += 1


    cv2.imshow("img", img)
    cv2.waitKey(1)




