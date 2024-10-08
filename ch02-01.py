import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Draw a line (start point (x1, y1), end point (x2, y2), color (BGR), thickness)
cv2.line(image, (100, 100), (400, 400), (0, 255, 0), 5)

plt.imshow(image)
plt.show()