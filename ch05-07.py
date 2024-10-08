import cv2
import numpy as np


def adjust_brightness_contrast_add_weighted(val):
    brightness = cv2.getTrackbarPos('Brightness', 'Image') - 50
    contrast = cv2.getTrackbarPos('Contrast', 'Image') / 50.0

    # Adjust brightness and contrast using cv2.addWeighted
    adjusted_img = cv2.addWeighted(img, contrast, np.zeros_like(img), 0, brightness)

    cv2.imshow('Image', adjusted_img)


img = cv2.imread('resources/lena.bmp')

cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)

# Create a trackbar (for brightness and contrast adjustment)
cv2.createTrackbar('Brightness', 'Image', 50, 100, adjust_brightness_contrast_add_weighted)
cv2.createTrackbar('Contrast', 'Image', 50, 100, adjust_brightness_contrast_add_weighted)

# Display initial image
adjust_brightness_contrast_add_weighted(0)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()