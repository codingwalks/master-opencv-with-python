import cv2


# Trackbar callback function (frame change)
def on_trackbar(val):
    global cap
    cap.set(cv2.CAP_PROP_POS_FRAMES, val)


# Load video file
cap = cv2.VideoCapture('resources/TownCentreXVID.mp4')

# Check if the video file is opened
if not cap.isOpened():
    print("Error: Unable to open video file")
    exit()

# Total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a window and set up the trackbar
cv2.namedWindow('Video Control')
cv2.createTrackbar('Frame', 'Video Control', 0, total_frames - 1, on_trackbar)

while True:
    ret, frame = cap.read()

    # End when end of video file is reached
    if not ret:
        break

    # Set current trackbar position
    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.setTrackbarPos('Frame', 'Video Control', current_frame)

    # Frame display
    cv2.imshow('Video Control', frame)

    # Exit with ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()