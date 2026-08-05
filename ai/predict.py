import os

from ai.face_detector import detect_and_crop
from ai.preprocess import preprocess
from ai.deepfake_model import predict as model_predict


def predict_image(file_path):
    """
    Predict whether the uploaded image is Real or Fake.

    Input:
        file_path (str): Path to the uploaded image

    Output:
        {
            "status": "...",
            "confidence": ...
        }
    """

    face = detect_and_crop(file_path)

    if face is None:
        return {
            "status": "No Face Detected",
            "confidence": 0
        }

    face_tensor = preprocess(face)

    return model_predict(face_tensor)


# Local testing only
if __name__ == "__main__":
    current_folder = os.path.dirname(__file__)
    image_path = os.path.join(current_folder, "test.png")

    result = predict_image(image_path)

    print("Prediction")
    print(result)