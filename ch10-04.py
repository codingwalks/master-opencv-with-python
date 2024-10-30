import cv2
import numpy as np

def apply_sharpening(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def apply_unsharp_mask(image):
    gaussian = cv2.GaussianBlur(image, (5,5), 2)
    return cv2.addWeighted(image, 1.5, gaussian, -0.5, 0)

# Load an image
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Apply filters
sharpened = apply_sharpening(image)
unsharpened = apply_unsharp_mask(image)

# Display the results
cv2.imshow('Sharpened', sharpened)
cv2.imshow('Unsharp Mask', unsharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()