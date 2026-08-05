import cv2

def preprocess(face):
    """
    Resize and normalize the face image
    """

    # Resize to 224x224
    face = cv2.resize(face, (224, 224))

    # Normalize pixel values (0-255 → 0-1)
    face = face / 255.0

    return face