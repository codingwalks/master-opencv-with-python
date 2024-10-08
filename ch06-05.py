import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image (convert to black and white image)
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(10, 5), linewidth=2)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

# Show graph
plt.tight_layout()
plt.savefig('results/hist_equalize1.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()