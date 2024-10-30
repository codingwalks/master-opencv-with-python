import cv2
import numpy as np

# Load an image
img = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Define a Gaussian blur kernel
kernel_blur = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]]) / 16

# Apply Gaussian blur using convolution
blurred_img = cv2.filter2D(img, -1, kernel_blur)

# Define a sharpening kernel
kernel_sharpen = np.array([[-1, -1, -1],
                         [-1, 9, -1],
                         [-1, -1, -1]])

# Apply sharpening using convolution
sharpened_img = cv2.filter2D(img, -1, kernel_sharpen)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', blurred_img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()