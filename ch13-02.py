import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('resources/image021.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarization (using Otsu's thresholding)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Noise removal (open operation)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Expanding the object area (dilation operation)
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Finding the exact area of an object using distance transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Finding boundary area by difference between clear object area and background area
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Create marker
_, markers = cv2.connectedComponents(sure_fg)

# Add 1 to the marker to set the background to 1
markers = markers + 1

# Set the boundary area as a marker
markers[unknown == 255] = 0

# apply watershed
markers = cv2.watershed(image, markers)
image[markers == -1] = [255, 0, 0]

titles = ['Gray', 'Binary', 'Sure BG', 'Distance', 'Sure FG', 'Unknown', 'Markers', 'Result']
images = [gray, thresh, sure_bg, dist_transform, sure_fg, unknown, markers, image]

plt.figure(figsize=(10, 5))
for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()