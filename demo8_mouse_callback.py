import cv2
import math

center = [0, 0]
circlefence = [(0, 0)]


def drawCircle(action, x, y, flags, userData):
    global center
    global circlefence
    # print(f"[{action}],[{x}],[{y}]")
    # print(cv2.EVENT_LBUTTONDOWN, cv2.EVENT_LBUTTONUP)
    if action == cv2.EVENT_LBUTTONDOWN:
        center = [(x, y)]
        cv2.circle(sourceImage, center[0], 1, (255, 255, 0), 6, cv2.LINE_AA)
    elif action == cv2.EVENT_LBUTTONUP:
        circlefence = [(x, y)]
        radius = math.sqrt(math.pow(center[0][0] - circlefence[0][0], 2) +
                           math.pow(center[0][1] - circlefence[0][1], 2))
        cv2.circle(sourceImage, center[0], int(radius), (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("window", sourceImage)
    pass


sourceImage = cv2.imread("./photos/background.jpg", 1)

dummy = sourceImage.copy()
cv2.namedWindow("window")
cv2.setMouseCallback("window", drawCircle)

k = 0
while k != 27:
    cv2.imshow("window", sourceImage)
    k = cv2.waitKey(50) & 0xFF
cv2.destroyAllWindows()
