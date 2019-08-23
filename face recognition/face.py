import face_recognition
import cv2                                                  
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


aarav_image = face_recognition.load_image_file("faces/Aarav.jpg")
josh_image = face_recognition.load_image_file("faces/Josh.jpg")
zach_image = face_recognition.load_image_file("faces/Zach.jpg")
cedric_image = face_recognition.load_image_file("faces/Cedric.jpg")
alex_image = face_recognition.load_image_file("faces/Alex.jpg")
bhaveeth_image = face_recognition.load_image_file("faces/Bhaveeth.jpg")

aarav_encoding = face_recognition.face_encodings(aarav_image)[0]
cedric_encoding = face_recognition.face_encodings(cedric_image)[0]
josh_encoding = face_recognition.face_encodings(josh_image)[0]
zach_encoding = face_recognition.face_encodings(zach_image)[0]
alex_encoding = face_recognition.face_encodings(alex_image)[0]
bhaveeth_encoding = face_recognition.face_encodings(bhaveeth_image)[0]

known_face_encodings = [
    aarav_encoding, 
    cedric_encoding,
    josh_encoding,
    zach_encoding,
    alex_encoding,
    bhaveeth_encoding
]

known_face_names = [
    "Aarav",
    "Cedric",
    "Josh",
    "Zach",
    "Alex",
    "Bhaveeth"
]

face_locations = []
face_encodings = []
face_names = []
process_this_img = True

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb_img = small_img[:, :, ::-1]
    if process_this_img:
        face_locations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.face_distance(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_img = not process_this_img

    for(top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        left *= 4
        bottom *= 4
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(img, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    cv2.imshow('Faces', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break