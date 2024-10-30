import cv2
import numpy as np

# Open WebCam
cap = cv2.VideoCapture(1)

while True:
    # Reading the frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and apply blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Binarization (thresholding)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Ignore objects that are too small
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

            # Calculating center of gravity
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    # Show frame
    gray_3channel = cv2.resize(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), (0,0), None, .5, .5)
    blurred_3channel = cv2.resize(cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR), (0,0), None, .5, .5)
    thresh_3channel = cv2.resize(cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR), (0,0), None, .5, .5)
    frame_resize = cv2.resize(frame, (0,0), None, .5, .5)
    result = np.vstack((np.hstack((gray_3channel, blurred_3channel)),np.hstack((thresh_3channel, frame_resize))))
    cv2.imshow("Object Tracking", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()