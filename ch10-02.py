import cv2

def apply_blurring(image):
    # Average Blur
    avg_blur = cv2.blur(image, (5, 5))
    # Gaussian Blur
    gauss_blur = cv2.GaussianBlur(image, (5, 5), 0)
    # Median Blur
    median_blur = cv2.medianBlur(image, 5)
    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 5, 75, 75)
    return avg_blur, gauss_blur, median_blur, bilateral

# Load an image
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Apply blurring techniques
avg, gauss, median, bilateral = apply_blurring(image)

# Display the results
cv2.imshow('Average Blur', avg)
cv2.imshow('Gaussian Blur', gauss)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()