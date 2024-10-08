import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image (convert to black and white image)
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Create a mask (calculate histogram for only a part of the image)
mask = np.zeros(image.shape[:2], np.uint8)
mask[128:384, 128:384] = 255

# Calculating histogram using mask
masked_hist = cv2.calcHist([image], [0], mask, [256], [0, 256])

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(10, 5), linewidth=2)

# Show Image
show_image = cv2.subtract(mask, 255-image)
plt.subplot(1, 2, 1)
plt.imshow(show_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Histogram plot
plt.subplot(1, 2, 2)
plt.plot(masked_hist)
plt.title('Masked Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Show plot
plt.tight_layout()
plt.savefig('results/hist3.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()