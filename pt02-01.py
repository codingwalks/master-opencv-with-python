import cv2
import numpy as np
import time

hsv_target_colors = {
    'orange':[5, 107, 0, 19, 255, 255],
    'purple':[133, 56, 0, 159, 156, 255],
    'green':[57, 76, 0, 100, 255, 255],
}
bgr_target_colors = {
    'orange':[51, 153, 255],
    'purple':[255, 0, 255],
    'green':[0, 255, 0],
}

color_trails = {
    'orange':[],
    'purple':[],
    'green':[],
}

# Trajectory disappearance time and trajectory maximum length
trail_lifetime = 2
max_trail_length = 30

cap = cv2.VideoCapture(0)

def find_color(img_hsv, target_colors, trail_list):
    current_time = time.time()
    for key in trail_list:
        lower = np.array(target_colors[key][0:3])
        upper = np.array(target_colors[key][3:6])
        trails = trail_list[key]
        # Create a mask
        mask = cv2.inRange(img_hsv, lower, upper)
        # Color trajectory update
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 500:
                perimeter = cv2.arcLength(largest, True)
                approx = cv2.approxPolyDP(largest, 0.02 * perimeter, True)
                x, y, w, h = cv2.boundingRect(approx)
                trails.append(((int(x+w//2), int(y+h//2)), current_time))

        # Remove coordinates older than 5 seconds from trajectory
        trails = [(pos, t) for pos, t in trails if current_time - t < trail_lifetime]
        # List size limit
        trails = trails[-max_trail_length:]
        trail_list[key] = trails
    return trail_list

def draw_on_canvas(canvas_bgr, trail_list, target_colors):
    for key in trail_list:
        for i in range(1, len(trail_list[key])):
            cv2.line(canvas_bgr, trail_list[key][i - 1][0], trail_list[key][i][0], target_colors[key], 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    canvas = np.zeros(frame.shape, dtype="uint8")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_trails = find_color(hsv, hsv_target_colors, color_trails)

    draw_on_canvas(canvas, color_trails, bgr_target_colors)

    combined_view = np.hstack((frame, canvas))
    cv2.imshow("Frame | Palette", combined_view)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()