import cv2
import numpy as np


# Mouse event handler function
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            cv2.rectangle(param, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 255), 2)
        else:
            cv2.circle(param, (x, y), 5, (0, 0, 255), 2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at ({x}, {y})")
        cv2.circle(param, (x, y), 5, (0, 0, 0), 2)
    elif event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse moved at ({x}, {y})")
        cv2.circle(param, (x, y), 1, (0, 255, 0), 2)


# Create a blank image
img = 255 * np.ones((300, 300, 3), dtype=np.uint8)

# Create an empty window
cv2.namedWindow('Mouse Event Window')

# Setting the mouse callback function
cv2.setMouseCallback('Mouse Event Window', mouse_event, img)

while True:
    cv2.imshow('Mouse Event Window', img)
    # Exit with ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()