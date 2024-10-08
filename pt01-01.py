import cv2
import math

points_list = []

def mouse_points(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
        points_list.append((x, y))

image = cv2.imread('angle_finder.jpg')
cv2.imshow('Image', image)
cv2.setMouseCallback('Image', mouse_points)

while True:
    if len(points_list) % 3 == 0 and len(points_list) != 0:
        points_1 = points_list[-3]
        points_2 = points_list[-2]
        points_3 = points_list[-1]

        m1 = (points_2[1] - points_1[1]) / (points_2[0] - points_1[0])
        m2 = (points_3[1] - points_2[1]) / (points_3[0] - points_2[0])

        angle_radians = math.atan2(m2 - m1, 1 + m1 * m2)
        angle_degrees = round(math.degrees(angle_radians))

        cv2.line(image, points_1, points_2, (0, 0, 255), 2)
        cv2.line(image, points_2, points_3, (0, 0, 255), 2)
        cv2.putText(image, f"Angle: {angle_degrees} degrees", (points_2[0] - 40, points_1[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)

        cv2.imshow('Image', image)
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()