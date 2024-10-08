import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image (convert to black and white image)
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Calculating histograms
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(10, 5), linewidth=2)

# Show Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Histogram plot
plt.subplot(1, 2, 2)
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Show plot
plt.tight_layout()
plt.savefig('results/hist1.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()