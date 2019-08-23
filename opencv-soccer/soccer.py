import cv2


def overlap(ballX, ballY, ballRadius, goalX, goalY, goalWidth, goalHeight):
    if(goalX < ballX - ballRadius < goalX + goalWidth):
        if(goalY < ballY - ballRadius < goalY + goalHeight):
            return True
    return False

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:

    _, img = cap.read()

    img = cv2.flip(img, 1)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break