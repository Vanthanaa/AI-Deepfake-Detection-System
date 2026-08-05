import cv2
import os


def detect_and_crop(image_path):
    """
    Detects the first face in an image,
    crops it and returns the cropped face.
    """

    # Load Haar Cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    print("Faces detected:", len(faces))

    if len(faces) == 0:
        return None

    # Take first detected face
    x, y, w, h = faces[0]

    face = image[y:y+h, x:x+w]

    return face