import cv2
import numpy as np

# Create a blank image
image = np.zeros((512, 512, 3), np.uint8)

# Output English text
cv2.putText(image, 'OpenCV Text Example', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
# Output Korean text
cv2.putText(image, 'OpenCV 텍스트 예제', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Image Output
cv2.imshow('Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()