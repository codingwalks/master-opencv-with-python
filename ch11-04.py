import cv2
import numpy as np

img = cv2.imread('resources/circle.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1)

# Line detection using Hough transform
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 100, None, 150, 40, 20, 80)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # Draw outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # Draw center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Hough Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()