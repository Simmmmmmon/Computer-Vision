import cv2
import time


def display_fps():
    video_capture = cv2.VideoCapture(0)  # Open the default camera (index 0)

    frame_count = 0
    start_time = time.time()

    while True:
        _, frame = video_capture.read()

        # Display the FPS on the video frame
        fps = calculate_fps(frame_count, start_time)
        cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Webcam', frame)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def calculate_fps(frame_count, start_time):
    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        return frame_count / elapsed_time
    else:
        return 0.0

display_fps()