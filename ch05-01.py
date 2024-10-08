import cv2

# Load image in grayscale
img_gray = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Gray Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()