import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_stretching(img):
    # Calculate minimum and maximum pixel values of an image
    min_val = np.min(img)
    max_val = np.max(img)

    # Apply histogram stretching
    stretched = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched

# Load image (convert to black and white image)
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Histogram stretching
stretched_image = histogram_stretching(image)

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(20, 5), linewidth=2)

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Calculating histograms of original image
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.subplot(1, 4, 2)
plt.plot(hist, color='black')
plt.title('Original Image Histogram')

plt.subplot(1, 4, 3)
plt.imshow(stretched_image, cmap='gray')
plt.title('Stretched Image')
plt.axis('off')

# Calculating histograms of stretched image
stretched_hist = cv2.calcHist([stretched_image], [0], None, [256], [0, 256])
plt.subplot(1, 4, 4)
plt.plot(stretched_hist, color='black')
plt.title('Stretched Image Histogram')

# Show image
plt.tight_layout()
plt.savefig('results/hist_stretched.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()