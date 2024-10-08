import cv2

# Load image (convert to black and white image)
img1 = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('resources/airplane.bmp', cv2.IMREAD_GRAYSCALE)

# Resize images (scale to the same size)
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Merge image weights
blended_image = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()