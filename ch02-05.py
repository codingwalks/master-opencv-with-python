import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Draw a ellipse
cv2.ellipse(image, (256, 256), (150, 100), 45, 0, 360, (255, 0, 0), 3)

plt.imshow(image)
plt.show()s