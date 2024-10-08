import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Set polygon coordinates
pts = np.array([[100, 50], [200, 300], [70, 200]], np.int32)
pts = pts.reshape((-1, 1, 2))

# Drawing a polygon
cv2.polylines(image, [pts], True, (255, 0, 0), 3)

plt.imshow(image)
plt.show()