import cv2
import numpy as np

# Load image (convert to black and white image)
img = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Check the image size and create a gradient mask of the same size
height, width = img.shape[:2]

# Set the center coordinates and radius of the circle
center = (width // 2, height // 2)
radius = 200

# Create coordinates for creating gradients
X, Y = np.meshgrid(np.arange(width), np.arange(height))

# # Calculating distance from the center of the image
dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

# Calculating gradient using sigmoid function
scale = 0.05
gradient_mask = 1 / (1 + np.exp(-scale * (dist_from_center - radius)))
gradient_mask = gradient_mask * 255
gradient_mask = gradient_mask.astype(np.uint8)

# Subtraction operation
subtracted_image1 = cv2.subtract(img, gradient_mask)
subtracted_image2 = cv2.subtract(gradient_mask, img)

cv2.imshow('Original Image', img)
cv2.imshow('Gradient Mask', gradient_mask)
cv2.imshow('Subtracted Image1', subtracted_image1)
cv2.imshow('Subtracted Image2', subtracted_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()