import cv2

img = cv2.imread('resources/baboon.bmp')
cv2.imshow('Original Image', img)

# Check image size
print(img.shape) # (480, 500, 3)

# Resize image
img_nearest = cv2.resize(img, (100, 96), interpolation=cv2.INTER_NEAREST)
img_linear = cv2.resize(img, (100, 96), interpolation=cv2.INTER_LINEAR)
img_area = cv2.resize(img, (100, 96), interpolation=cv2.INTER_AREA)

cv2.imshow('Nearest Neighborhood Interpolation', img_nearest)
cv2.imshow('Linear Interpolation', img_linear)
cv2.imshow('Area-Based Interpolation', img_area)

# Check the adjusted image size
print(img_nearest.shape)  # (300, 200, 3)

cv2.waitKey(0)
cv2.destroyAllWindows()