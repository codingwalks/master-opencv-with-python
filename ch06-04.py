import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_pdf(img):
    # Calculating histograms (calculating the frequency of pixel values)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # Convert each bin to a probability by dividing it by the total number of pixels.
    pdf = hist / np.sum(hist)
    return pdf

def calculate_cdf(pdf):
    # Compute CDF by accumulating PDFs
    cdf = np.cumsum(pdf)
    # Normalize to 0~1 range
    cdf_normalized = cdf / cdf.max()
    return cdf_normalized

# Load image (convert to black and white image)
image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# PDF Calculation
pdf = calculate_pdf(image)

# CDF calculation
cdf = calculate_cdf(pdf)

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(15, 5), linewidth=2)

# Show Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# PDF plot
plt.subplot(1, 3, 2)
plt.plot(pdf, color='blue')
plt.title('PDF (Probability Density Function)')
plt.xlabel('Pixel Value')
plt.ylabel('Probability')

# CDF plot
plt.subplot(1, 3, 3)
plt.plot(cdf, color='green')
plt.title('CDF (Cumulative Distribution Function)')
plt.xlabel('Pixel Value')
plt.ylabel('Cumulative Probability')

# Show graph
plt.tight_layout()
plt.savefig('results/pdf_cdf.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()