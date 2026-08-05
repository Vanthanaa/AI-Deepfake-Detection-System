import os

from face_detector import detect_and_crop
from preprocess import preprocess
from deepfake_model import predict

current_folder = os.path.dirname(__file__)

image_path = os.path.join(current_folder, "test.png")

face = detect_and_crop(image_path)

if face is None:
    print("No face detected")
    exit()

processed = preprocess(face)

result = predict(processed)

print()

print("Prediction")

print(result)
