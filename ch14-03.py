import cv2

# Reading and binarizing images
image = cv2.imread('resources/approxpolydp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculating and Drawing the Convex Hull
for contour in contours:
    hull = cv2.convexHull(contour)
    cv2.drawContours(image, [hull], -1, (0, 0, 255), 2)

cv2.imshow('Convex Hull', image)
cv2.waitKey(0)
cv2.destroyAllWindows()