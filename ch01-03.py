import cv2

# load webcam (ID 0)
cap = cv2.VideoCapture(0)

# video save settings
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('webcam_output.avi', fourcc, 20.0, (640, 480))

# set resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)# width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)# height

while True:
    # read frame
    success, img = cap.read()

    # show frame
    cv2.imshow('Webcam', img)

    # save frame
    out.write(img)

    # end loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# disable webcam and video and close window
cap.release()
out.release()
cv2.destroyAllWindows()