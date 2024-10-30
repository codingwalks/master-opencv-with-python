import cv2
import numpy as np

def apply_emboss(image):
    # Embossing kernel
    kernel = np.array([[-1, -1, 0],
                       [-1, 0, 1],
                       [0, 1, 1]])

    return cv2.filter2D(image, -1, kernel, anchor=(-1,-1), delta=128)


# Load an image
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Apply embossing filter
embossed = apply_emboss(image)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Embossed Image', embossed)
cv2.waitKey(0)
cv2.destroyAllWindows()