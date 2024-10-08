import cv2

# Load a color image
img_color = cv2.imread('resources/lena.bmp')

# Convert color image to grayscale
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()