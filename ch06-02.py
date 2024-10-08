import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image (color image)
image = cv2.imread('resources/lena.bmp')

# Plotting PDF and CDF (Matplotlib)
plt.figure(figsize=(10, 5), linewidth=2)

# Show Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('RGB Image')
plt.axis('off')

# Calculate histogram (for each channel)
plt.subplot(1, 2, 2)
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Color Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Show plot
plt.tight_layout()
plt.savefig('results/hist2.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()