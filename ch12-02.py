import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resources/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

th_adap_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,45,5)
th_adap_gaussian = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,45,5)

titles = ['Original','Mean','Gaussian']
images = [img,th_adap_mean,th_adap_gaussian]

plt.figure(figsize=(10, 4))
for i in range(len(images)):
	plt.subplot(1,3,i+1), plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()