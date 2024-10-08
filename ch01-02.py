import cv2

# load video
cap = cv2.VideoCapture('resources/TownCentreXVID.mp4')

while True:
    # reading the frame
    success, img = cap.read()

    # check if the frame was read successfully
    if not success:
        break

    # show frame
    cv2.imshow('Video', img)

    # end loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video object and close the window
cap.release()
cv2.destroyAllWindows()