import cv2

# Reading and binarizing images
image = cv2.imread('resources/approxpolydp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Select one of the outlines and apply an approximate polygon
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Draw approximate contours
    cv2.drawContours(image, [approx], -1, (0, 0, 255), 2)

cv2.imshow('Approx PolyDP', image)
cv2.waitKey(0)
cv2.destroyAllWindows()