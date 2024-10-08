import cv2
import numpy as np

# Trackbar callback function
def on_trackbar(val):
    print(f"Trackbar value: {val}")

cv2.namedWindow('Trackbar Window')

# Create trackbar (name, window name, initial value, maximum value, callback function)
cv2.createTrackbar('Slider', 'Trackbar Window', 0, 100, on_trackbar)

while True:
    img = 255 * np.ones((300, 300, 3), dtype=np.uint8)
    cv2.imshow('Trackbar Window', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()