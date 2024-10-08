import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Increase brightness (add constant)
bright_img = np.clip(cv2.add(img, 100), 0, 255).astype(np.uint8)

# Increase contrast (multiply by a constant)
contrast_img = np.clip(cv2.multiply(img, 1.5), 0, 255).astype(np.uint8)

plt.figure(figsize=(15, 4), linewidth=2)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(bright_img, cmap='gray')
plt.title('Bright Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(contrast_img, cmap='gray')
plt.title('Contrast Image')
plt.axis('off')

# Show plot
plt.tight_layout()
plt.savefig('results/arithmetic.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()