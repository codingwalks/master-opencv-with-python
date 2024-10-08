import cv2
import numpy as np

# A function that adjusts the brightness and contrast of an image
def adjust_brightness_contrast(val):
    brightness = cv2.getTrackbarPos('Brightness', 'Image') - 50
    contrast = cv2.getTrackbarPos('Contrast', 'Image') / 50.0

    # Brightness and contrast control
    adjusted_img = np.int16(img)
    adjusted_img = adjusted_img * contrast + brightness
    adjusted_img = np.clip(adjusted_img, 0, 255)  # 값 범위를 0-255로 제한
    adjusted_img = np.uint8(adjusted_img)

    cv2.imshow('Image', adjusted_img)

img = cv2.imread('resources/lena.bmp')

cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)

# Create a trackbar (for brightness and contrast adjustment)
cv2.createTrackbar('Brightness', 'Image', 50, 100, adjust_brightness_contrast)
cv2.createTrackbar('Contrast', 'Image', 50, 100, adjust_brightness_contrast)

# Display initial image
adjust_brightness_contrast(0)

while True:
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키를 누르면 종료
        break

cv2.destroyAllWindows()