import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Draw a rectangle
cv2.rectangle(image, (50, 50), (450, 450), (255, 0, 0), 3)

plt.imshow(image)
plt.show()