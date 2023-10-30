import mediapipe as mp
import cv2
import time

cap =cv2.VideoCapture(0)
frame_count = 0
start_time = time.time()

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
FaceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
DrawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True :
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    Results = FaceMesh.process(imgRGB)
    if Results.multi_face_landmarks :
        for faceLms in  Results.multi_face_landmarks :
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,DrawSpec,DrawSpec)
            for id,lm in enumerate(faceLms.landmark) :
                # print(lm)
                h, w, c = img.shape
                x,y = int(lm.x*w), int(lm.y*h)
                print(id, x, y)


    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        fps = int(frame_count / elapsed_time)
    else:
        fps = 0

    cv2.putText(img, str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    frame_count += 1


    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
