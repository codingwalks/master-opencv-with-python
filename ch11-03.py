import cv2
import numpy as np

img = cv2.imread('resources/building.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# Line detection using Hough transform
lines_p = cv2.HoughLinesP(edges, 1, np.pi / 180, 160, None, 50, 5)

# Draw the detected straight line
results = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
if lines_p is not None:
    for line in lines_p:
        x1, y1, x2, y2 = line[0]
        cv2.line(results, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Hough Lines', results)
cv2.waitKey(0)
cv2.destroyAllWindows()