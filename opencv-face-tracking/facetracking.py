import cv2
import time
import random

CAPTURE_WIDTH = 1280
CAPTURE_HEIGHT = 720
cap = cv2.VideoCapture(0)
cap.set(3,CAPTURE_WIDTH)
cap.set(4, CAPTURE_HEIGHT)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

time.sleep(1)

points = 0 
hit_target = True
targetX = 0
targetY = 0
targetW = 69


while(True):
    _, img = cap.read()
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (72, 212, 212), 3)

        if (targetX >= x and targetX <= x + w) and (y <= targetY <= y + h):
            hit_target = True
            points += 1

    if hit_target:
        targetX = random.randint(targetW, CAPTURE_WIDTH - targetW)
        targetY = random.randint(targetW, CAPTURE_HEIGHT - targetW)
        hit_target = False

    cv2.rectangle(img, (targetX, targetY), (targetX + targetW, targetY + targetW), (28, 252, 3), 20)

    cv2.putText(img, "Points: " + str(points), (0, 50), cv2. FONT_HERSHEY_DUPLEX, 1, (3, 252, 28), 2)
    cv2.imshow('Face Tracking', img)

    cv2.imshow('Face Tracking', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
