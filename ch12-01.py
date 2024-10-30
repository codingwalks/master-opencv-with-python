import cv2
import matplotlib.pyplot as plt

img = cv2.imread('resources/lena.bmp', cv2.IMREAD_GRAYSCALE)

ret, th_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th_trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th_tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th_tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['ORIGINAL', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th_binary, th_binary_inv, th_trunc, th_tozero, th_tozero_inv]

plt.figure(figsize=(10, 7))
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()