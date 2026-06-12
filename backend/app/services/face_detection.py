import cv2
import numpy as np

## Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_bytes):

    numpy_array = np.frombuffer(image_bytes, np.uint8)
    openvc_image = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)

    grayscale_image = cv2.cvtColor(openvc_image, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(openvc_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    _, encoded_image = cv2.imencode('.jpg', openvc_image)
    return encoded_image.tobytes()

def detect_faces_video(video_path, output_path):
    video = cv2.VideoCapture(video_path)

    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    
    while True:
        success, frame = video.read()
        if not success:
            break 

        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        faces = face_cascade.detectMultiScale(grayscale_frame, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        video_writer.write(frame)
    video.release()
    video_writer.release()


def detect_face_webcam(cv_image):
    grayscale_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    _, encoded_image = cv2.imencode('.jpg', cv_image)
    return encoded_image.tobytes()
   