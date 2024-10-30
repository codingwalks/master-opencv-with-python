import cv2

# Reading and binarizing images
image = cv2.imread('resources/contour.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.namedWindow('Contours', flags=cv2.WINDOW_AUTOSIZE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()