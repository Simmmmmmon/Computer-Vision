import cv2
import time






def display_fps(video_capture):
    frame_count = 0
    start_time = time.time()

    while True:
        _, frame = video_capture.read()

        frame_count += 1
        elapsed_time = time.time() - start_time


        if elapsed_time >= 1:
            fps = frame_count / elapsed_time
            print(int(fps))
            frame_count = 0
            start_time = time.time()

video_capture = cv2.VideoCapture(0)  # Change the index or video file path if needed
display_fps(video_capture)