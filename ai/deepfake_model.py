import os
import torch
from ai.model import DeepfakeClassifier

# Use CPU
device = torch.device("cpu")

# Create model
model = DeepfakeClassifier(backbone="b4")

# Load trained weights
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "best_model.pt")
checkpoint = torch.load(model_path, map_location=device)

# Some checkpoints store only weights, others store a dictionary
if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
    model.load_state_dict(checkpoint["model_state_dict"])
else:
    model.load_state_dict(checkpoint)

model.to(device)
model.eval()


def predict(face_tensor):
    """
    Predict whether the face is Real or Fake.
    face_tensor must be a PyTorch tensor of shape [1, 3, 224, 224]
    """

    with torch.no_grad():
        output = model(face_tensor)
        probability = torch.sigmoid(output).item()

    if probability >= 0.5:
        return {
            "status": "Fake",
            "confidence": round(probability * 100, 2)
        }
    else:
        return {
            "status": "Real",
            "confidence": round((1 - probability) * 100, 2)
        }