import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('resources/j_image.png', cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(image, (3, 3), 0)
# blur = cv2.medianBlur(image, 3)
ret, thresh = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY)

# thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 5)

# Kernel definition (size 5x5)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion operation
erosion = cv2.erode(thresh, kernel, iterations=1)

# Applying dilation operation
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Apply opening operation
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Apply closing operation
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Apply gradient operation
gradient = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)

titles = ['Original', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient']
images = [thresh, erosion, dilation, opening, closing, gradient]

plt.figure(figsize=(10, 7))
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()