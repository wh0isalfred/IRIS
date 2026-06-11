import cv2
import numpy as np

def detect_faces(image_bytes):

    numpy_array = np.frombuffer(image_bytes, np.uint8)
    openvc_image = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)

    grayscale_image = cv2.cvtColor(openvc_image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(openvc_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    _, encoded_image = cv2.imencode('.jpg', openvc_image)
    return encoded_image.tobytes()