import cv2

# Load image in grayscale
gray = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Contrast and brightness control (increase contrast)
alpha = 1.5  # Contrast ratio
beta = 0.0   # Contrast ratio (0 means no change)
gamma = 50   # Brightness to add

# Adjust brightness and contrast ratio with addWeighted function
adjusted_img = cv2.addWeighted(gray, alpha, gray, beta, gamma)

cv2.imshow('Brightness/Contrast Adjusted', adjusted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()