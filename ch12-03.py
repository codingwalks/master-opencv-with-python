import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resources/noisy_leaf.jpg', cv2.IMREAD_GRAYSCALE)
img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])

ret, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (9, 9), 0)
blur_hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
ret, blur_otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(10, 7), linewidth=2)

plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original Noisy Image')
plt.axis('off')
plt.subplot(2, 3, 2), plt.plot(img_hist, color='black')
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.subplot(2, 3, 3), plt.imshow(otsu, cmap='gray')
plt.title('Otsu\'s Thresholding')
plt.axis('off')

plt.subplot(2, 3, 4), plt.imshow(blur, cmap='gray')
plt.title('Gaussian Filtered Image')
plt.axis('off')
plt.subplot(2, 3, 5), plt.plot(blur_hist, color='black')
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.subplot(2, 3, 6), plt.imshow(blur_otsu, cmap='gray')
plt.title('Otsu\'s Thresholding')
plt.axis('off')

plt.tight_layout()
plt.show()