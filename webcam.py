import cv2
import sys

# We Will is this Cascading Fiter
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Starting the Cideo Capture
video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detecting the face
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    try:
        if len(faces[0]) >0:
            # Capturing the Pic of the Culprit LoL
            r,frame = video_capture.read()
            if r:
                cv2.imwrite("Intruder.png",frame)
                break
            else:
                continue
    except:
        continue