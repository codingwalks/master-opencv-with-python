import cv2
import matplotlib.pyplot as plt

# Load image (convert to grayscale image)
image = cv2.imread('resources/x-ray.jpg', cv2.IMREAD_GRAYSCALE)

# Apply basic histogram equalization
equalized_image = cv2.equalizeHist(image)

# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(image)

plt.figure(figsize=(16, 8))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Equalization')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(clahe_image, cmap='gray')
plt.title('CLAHE')
plt.axis('off')

plt.tight_layout()
plt.savefig('results/hist_equalize3.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()