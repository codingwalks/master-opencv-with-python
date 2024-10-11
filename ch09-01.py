import cv2

image_bgr = cv2.imread('resources/lena.bmp')

# Channel splitting (BGR)
blue_channel, green_channel, red_channel = cv2.split(image_bgr)

import matplotlib.pyplot as plt
plt.figure(figsize=(25, 5), linewidth=2)

plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(blue_channel, cmap='gray')
plt.title('Blue Channel Image')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(green_channel, cmap='gray')
plt.title('Green Channel Image')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(red_channel, cmap='gray')
plt.title('Red Channel Image')
plt.axis('off')

# Set the blue channel to 0 and merge
blue_channel[:] = 0
modified_image = cv2.merge([blue_channel, green_channel, red_channel])

plt.tight_layout()
plt.savefig('results/color_channels.png', dpi=200, facecolor='#eeeeee', edgecolor='black')
plt.show()

# cv2.imshow('Modified Image', modified_image)
cv2.imwrite('results/color_modified.png', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()