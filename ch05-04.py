import cv2
import numpy as np

# Load image in grayscale
gray = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

gray_dec = np.clip(gray*0.5, 0, 255).astype(np.uint8)
gray_inc = np.clip(gray*2.0, 0, 255).astype(np.uint8)
result = cv2.hconcat([gray, gray_dec, gray_inc])

cv2.imshow('Contrast Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()