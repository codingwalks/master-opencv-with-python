import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_pdf(img):
    # Calculating histograms
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # Convert to probability by dividing by total number of pixels (PDF)
    pdf = hist / np.sum(hist)
    return hist, pdf

def calculate_cdf(pdf):
    cdf = np.cumsum(pdf)
    # Normalize to 0~1 range
    cdf_normalized = cdf / cdf.max()
    return cdf_normalized

# Calculating and applying CDF during histogram equalization process
def histogram_equalization(img):
    # PDF Calculation
    hist, pdf = calculate_pdf(img)
    # CDF Calculation
    cdf = calculate_cdf(pdf)
    # Mapping pixel values using CDF
    return hist, np.round(np.interp(img.flatten(), range(256), cdf*255)).reshape(img.shape).astype(np.uint8)

# Load image (convert to black and white image)
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
hist, equalized_image = histogram_equalization(image)

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(20, 5), linewidth=2)

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.plot(hist, color='black')
plt.title('Original Image Histogram')

plt.subplot(1, 4, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

# Calculating histograms of eqaulized image
equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plt.subplot(1, 4, 4)
plt.plot(equalized_hist, color='black')
plt.title('Equalized Image Histogram')

# Show graph
plt.tight_layout()
plt.savefig('results/hist_equalize2.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()