import cv2

img = cv2.imread('resources/baboon.bmp')
cv2.imshow('Original Image', img)

# Check image size
print(img.shape) # (480, 500, 3)

# Resize image
img_nearest = cv2.resize(img, (2500, 2400), interpolation=cv2.INTER_NEAREST)
img_linear = cv2.resize(img, (2500, 2400), interpolation=cv2.INTER_LINEAR)
img_cubic = cv2.resize(img, (2500, 2400), interpolation=cv2.INTER_CUBIC)
img_lanczos = cv2.resize(img, (2500, 2400), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('Nearest Neighborhood Interpolation', img_nearest)
cv2.imshow('Linear Interpolation', img_nearest)
cv2.imshow('Cubic Interpolation', img_cubic)
cv2.imshow('Lanczos Interpolation', img_lanczos)

# Check the adjusted image size
print(img_nearest.shape)  # (2400, 2500, 3)

cv2.waitKey(0)
cv2.destroyAllWindows()