import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Polygon Coordinates
pts1 = np.array([[100, 50], [200, 300], [70, 200]], np.int32)
pts2 = np.array([[300, 200], [400, 400], [250, 350]], np.int32)

cv2.fillPoly(image, [pts1, pts2], (255, 0, 0))

plt.imshow(image)
plt.show()