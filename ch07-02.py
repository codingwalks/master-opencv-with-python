import cv2
import numpy as np

# Load image
img1 = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('resources/baboon.bmp', cv2.IMREAD_GRAYSCALE)

# Resize images (scale to the same size)
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Image addition operation
added_image = np.clip(cv2.add(img1, img2), 0, 255).astype(np.uint8)

cv2.imshow('Added Image', added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()