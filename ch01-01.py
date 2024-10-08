import cv2

# load image
img = cv2.imread('resources/Lena_Color.png')

# show image
cv2.imshow('Output', img)

# Keep screen on (0 means infinite wait)
cv2.waitKey(0)