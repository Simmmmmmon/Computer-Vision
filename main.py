import cv2

img = cv2.imread('background.png')
if img is None:
    print("Image not loaded!")
else:
    print("Image is loaded!")