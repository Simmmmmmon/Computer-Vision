import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self):
 # mode=False, maxHands = 2, dectectionCon =0.5, trackCon = 0.5
 #        self.mode = mode
 #        self.maxHands = maxHands
 #        self.detectionCon = dectectionCon
 #        self.trackCon = trackCon
# self.mode, self.maxHands, self.detectionCon, self.trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks :
            for handLms in results.multi_hand_landmarks :
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


def main():
    frame_count = 0
    start_time = time.time()
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        elapsed_time = time.time() - start_time
        if elapsed_time > 0:
            fps = int(frame_count / elapsed_time)
        else:
            fps = 0

        cv2.putText(img, str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        frame_count += 1
        cv2.imshow("Image", img)
        cv2.waitKey(1)




def calculate_fps(frame_count, start_time):
    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        return frame_count / elapsed_time
    else:
        return 0.0


if __name__ == "__main__":
    main()