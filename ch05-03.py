import cv2
import numpy as np

# Load image in grayscale
gray = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)
gray_minus = np.clip(gray-100, 0, 255).astype(np.uint8)
gray_plus = np.clip(gray+100, 0, 255).astype(np.uint8)

result = cv2.hconcat([gray, gray_minus, gray_plus])

cv2.imshow('Brightness Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()