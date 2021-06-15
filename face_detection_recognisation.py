import pathlib
import cv2  # Used for detecting face only frames
import winsound  # Used for playing alarm after recognizing of criminal
import time  # Used for fetching the current system time
from azure_recognisation import azure_recognisation
from send_text import send_text_to_authority


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)


# Defining detectFace() method for capturing photo frames containing face

def detect_face(face_client, sms_client):
    while True:
        flag = False

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        k = cv2.waitKey(1)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if frame.any():
                flag = True

        # Display the resulting frame
        cv2.imshow("Beat The Culprits", frame)
        if flag:
            when_flag_is_true(frame, face_client, sms_client)


def when_flag_is_true(frame, face_client, sms_client):
    time_stamp = time.time()
    cv2.imwrite(filename=str(time_stamp) + '.jpg', img=frame)
    image = open(str(time_stamp) + '.jpg', 'r+b')
    response = azure_recognisation(face_client, image)
    if response == "-1":
        print("Not a criminal")
        try:
            image.close()
            file_to_rem = pathlib.Path(str(time_stamp) + '.jpg')
            file_to_rem.unlink()
        except:
            print("Error while deleting the file")

    else:
        send_text_to_authority(sms_client, response)
        winsound.PlaySound('SirenNoise.wav', winsound.SND_FILENAME)
        time.sleep(5)


# def stop_detection():
# video_capture.release()
# cv2.destroyAllWindows()
