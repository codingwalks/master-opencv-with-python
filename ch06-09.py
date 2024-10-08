import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_pdf(img):
    # Calculating histograms (calculating the frequency of pixel values)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # Convert each bin to a probability by dividing it by the total number of pixels.
    pdf = hist / np.sum(hist)
    return hist, pdf

def calculate_cdf(pdf):
    # Compute CDF by accumulating PDFs
    cdf = np.cumsum(pdf)
    # Normalize to 0~1 range
    cdf_normalized = cdf / cdf.max()
    return cdf_normalized

def histogram_matching(source, target):
    # Calculating PDF
    source_hist, source_pdf = calculate_pdf(source)
    target_hist, target_pdf = calculate_pdf(target)

    # Calculating CDF
    source_cdf_normalized = calculate_cdf(source_pdf)
    target_cdf_normalized = calculate_cdf(target_pdf)

    # Create a matching table
    mapping = np.interp(source_cdf_normalized, target_cdf_normalized, np.arange(256))

    # Apply matching results
    matched_image = mapping[source.flatten()].reshape(source.shape)
    return source_hist, target_hist, matched_image.astype(np.uint8)

source_image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)
target_image = cv2.imread('resources/airplane.bmp', cv2.IMREAD_GRAYSCALE)

source_hist, target_hist, matched_image = histogram_matching(source_image, target_image)

# Plotting PDF and CDF (Matplotlib)
fig, axes = plt.subplots(2,3, figsize=(10,5))

axes[0][0].imshow(cv2.cvtColor(source_image, cv2.COLOR_GRAY2RGB))
axes[0][0].set_title('Source Image')
axes[0][0].axis('off')
axes[1][0].plot(source_hist, color='black')

axes[0][1].imshow(cv2.cvtColor(target_image, cv2.COLOR_GRAY2RGB))
axes[0][1].set_title('Target Image')
axes[0][1].axis('off')
axes[1][1].plot(target_hist, color='black')

axes[0][2].imshow(cv2.cvtColor(matched_image, cv2.COLOR_GRAY2RGB))
axes[0][2].set_title('Matched Image')
axes[0][2].axis('off')
matched_hist = cv2.calcHist([matched_image], [0], None, [256], [0, 256])
axes[1][2].plot(matched_hist, color='black')

# Show image
plt.tight_layout()
plt.savefig('results/hist_matched.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()