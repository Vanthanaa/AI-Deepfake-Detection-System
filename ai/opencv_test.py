import os
import cv2
from face_detector import detect_and_crop

current_folder = os.path.dirname(__file__)

image_path = os.path.join(current_folder, "test.png")

face = detect_and_crop(image_path)

if face is None:
    print("No face detected!")
else:
    print("Face extracted successfully!")

    cv2.imshow("Cropped Face", face)

    cv2.waitKey(0)

    cv2.destroyAllWindows()