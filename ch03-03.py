import cv2
import numpy as np

cv2.namedWindow('Keyboard Event Window')

while True:
    img = 255 * np.ones((300, 300, 3), dtype=np.uint8)
    cv2.imshow('Keyboard Event Window', img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Key 'q' pressed - Exiting")
        break
    elif key == ord('s'):
        print("Key 's' pressed - Saving image")
        cv2.imwrite('saved_image.jpg', img)

cv2.destroyAllWindows()