import cv2
import numpy as np


# Empty function to be used in the trackbar (for trackbar callbacks)
def empty(a):
    pass


image_bgr = cv2.imread('resources/fruits.bmp')

# HSV color space conversion
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# Create a trackbar window
cv2.namedWindow("Trackbars")

# Trackbar settings (Minimum and maximum values
# for Hue, Saturation, and Value, respectively)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)  # Hue ranges from 0 to 179
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)  # Saturation ranges from 0 to 255
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)  # Value is in the range of 0 to 255
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    # Read values from the trackbar
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    # Create arrays of minimum and maximum values
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Detect only colors within the HSV range with a mask
    mask = cv2.inRange(image_hsv, lower, upper)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)

    cv2.imshow("Original", image_bgr)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()