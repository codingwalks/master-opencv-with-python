import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

# Simple edge detection kernel
# Defining horizontal and vertical kernels
horizontal_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
vertical_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Apply convolution
horizontal_edges = cv2.filter2D(image, -1, horizontal_kernel)
vertical_edges = cv2.filter2D(image, -1, vertical_kernel)

# Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Laplacian operator
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Canny edge detection
canny_edges = cv2.Canny(image, 100, 200)

titles = ['Original', 'Horizontal Edges', 'Vertical Edges',
          'Sobel Operator', 'Laplacian Operator', 'Canny Edges']
images = [image, horizontal_edges, vertical_edges, sobel_magnitude, laplacian, canny_edges]

plt.figure(figsize=(10, 7))
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()