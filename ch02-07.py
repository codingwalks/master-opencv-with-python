import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Generate elliptical coordinates
ellipse_points = cv2.ellipse2Poly((256, 256), (150, 100), 45, 0, 360, 30)

# Drawing an ellipse with a polygon
cv2.polylines(image, [ellipse_points], True, (255, 0, 0), 3)

plt.imshow(image)
plt.show()