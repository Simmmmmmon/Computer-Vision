import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
frame_count = 0
start_time = time.time()

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
FaceDetection = mpFaceDetection.FaceDetection()

while True:
    success,  img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    Results = FaceDetection.process(imgRGB)
    print(Results)

    if Results.detections :
        for id, detection in enumerate(Results.detections):
            # mpDraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            h, w, c = img.shape
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                   int(bboxC.width * w), int(bboxC.height * h)

            cv2.rectangle(img, bbox, (240, 0 ,228), 2)
            cv2.putText(img, f"{int(detection.score[0] * 100)}%", (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 4, (240, 0 ,228), 2 )

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


