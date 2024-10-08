import cv2

img = cv2.imread('resources/baboon.bmp')
cv2.imshow('Original Image', img)

# Check image size
print(img.shape) # (480, 500, 3)

cropped_img = img[50:150,30:130]
cv2.imshow('Cropped Image', cropped_img)

# Check the cropped image size
print(cropped_img.shape)  # (100, 100, 3)

cv2.waitKey(0)
cv2.destroyAllWindows()