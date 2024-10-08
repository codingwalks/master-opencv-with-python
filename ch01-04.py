import cv2

# load RTSP streams
rtsp_url = 'rtsp://username:password@ip_address:port/stream'
cap = cv2.VideoCapture(rtsp_url)

# video save settings
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('rtsp_output.avi', fourcc, 20.0, (640, 480))

while True:
    success, frame = cap.read()
    if not success:
        break

    # streaming output
    cv2.imshow('Streaming', frame)

    # save frame
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# end stream save
cap.release()
out.release()
cv2.destroyAllWindows()