import cv2

# Reading and binarizing images
image = cv2.imread('resources/approxpolydp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculating moments for the first contour
for contour in contours:
    M = cv2.moments(contour)

    # Calculating area
    area = M["m00"]

    # Calculating center of gravity
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # Drawing contours and center of gravity
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)

cv2.imshow('Contours and Centroid', image)
cv2.waitKey(0)
cv2.destroyAllWindows()