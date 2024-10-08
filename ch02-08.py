import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convex polygon coordinates
pts = np.array([[150, 100], [200, 200], [100, 300], [50, 200]], np.int32)
cv2.fillConvexPoly(image, pts, (0, 255, 0))

plt.imshow(image)
plt.show()