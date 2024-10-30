import cv2

# Reading and binarizing images
image = cv2.imread('resources/contour.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Detecting edges in binarized images
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # Calculating moments
    M = cv2.moments(contour)

    # Calculating center of gravity
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        # Draw contours and mark center of gravity
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)

cv2.imshow("Labeled Objects with Moments", image)
cv2.waitKey(0)
cv2.destroyAllWindows()