import cv2
from matplotlib import pyplot as plt
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Draw a line only inside a rectangle
rect = (50, 50, 200, 200)# Definition of a square (x, y, width, height)
p1 = (0, 0)
p2 = (400, 400)

inside, clipped_p1, clipped_p2 = cv2.clipLine(rect, p1, p2)

if inside:
    cv2.line(image, clipped_p1, clipped_p2, (0, 0, 255), 3)

plt.imshow(image)
plt.show()