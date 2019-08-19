import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

time.sleep(1)

while(True):
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (72, 212, 212), 3)

    cv2.imshow('Face Tracking', img)

    if cv2.waitKey(1) & 0xF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
