import cv2
import numpy as np

# Load image (convert to black and white image)
img = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Check the image size and create a gradient mask of the same size
height, width = img.shape[:2]

mask = np.zeros((height, width), dtype=np.uint8)
cv2.circle(mask, (height//2, width//2), 200, 255, -1)
cv2.imshow('Mask', mask)

# Logical operations
bitwise_and = cv2.bitwise_and(img, mask)
bitwise_or = cv2.bitwise_or(img, mask)
bitwise_xor = cv2.bitwise_xor(img, mask)
bitwise_not = cv2.bitwise_not(img, mask)

cv2.imshow('Original Image', img)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.imshow('Bitwise NOT', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()