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
        center = (x, y)
        cv2.circle(sourceImage, center, 1, (255, 255, 0), 6, cv2.LINE_AA)
    elif action == cv2.EVENT_LBUTTONUP:
        circlefence = (x, y)
        radius = math.sqrt(math.pow(center[0] - circlefence[0], 2) +
                           math.pow(center[1] - circlefence[1], 2))
        cv2.circle(sourceImage, center, int(radius), (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("window", sourceImage)
    pass


sourceImage = cv2.imread("./photos/background.jpg", 1)

dummy = sourceImage.copy()
cv2.namedWindow("window")
cv2.setMouseCallback("window", drawCircle)

k = 0
while k != 27:
    cv2.imshow("window", sourceImage)
    cv2.putText(sourceImage, 'left click to decide center\n esc to leave, to plot circle',
                (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    k = cv2.waitKey(50) & 0xFF
    if k == ord('c'):
        sourceImage = dummy.copy()
cv2.destroyAllWindows()
