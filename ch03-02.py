import cv2
import numpy as np

# A function that handles all mouse events
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button down at ({x}, {y})")
    elif event == cv2.EVENT_LBUTTONUP:
        print(f"Left button released at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button down at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONUP:
        print(f"Right button released at ({x}, {y})")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print(f"Left button double clicked at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print(f"Right button double clicked at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(f"Middle button down at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONUP:
        print(f"Middle button released at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print(f"Middle button double clicked at ({x}, {y})")
    elif event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse moved to ({x}, {y})")
    elif event == cv2.EVENT_MOUSEWHEEL:
        print(f"Mouse wheel scrolled vertically at ({x}, {y})")
    elif event == cv2.EVENT_MOUSEHWHEEL:
        print(f"Mouse horizontal wheel scrolled at ({x}, {y})")

# Create an empty window
cv2.namedWindow('Mouse Event Window')

# Setting the mouse callback function
cv2.setMouseCallback('Mouse Event Window', mouse_event)

while True:
    # Display a blank image in the window
    img = 255 * np.ones((300, 300, 3), dtype=np.uint8)
    cv2.imshow('Mouse Event Window', img)

    # Exit with ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()