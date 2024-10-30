import cv2
import numpy as np

# Reading and binarizing images
image = cv2.imread('resources/contour.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# labeling
num_labels, labels_im = cv2.connectedComponents(binary)

# Colorize labels
label_hue = np.uint8(179 * labels_im / np.max(labels_im))
blank_ch = 255 * np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# Apply colormap (HUE -> BGR conversion)
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# Background is set to white
labeled_img[label_hue == 0] = 255

result = np.hstack((image, labeled_img))

cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()