import os
import torch
from ai.model import DeepfakeClassifier

# Use CPU
device = torch.device("cpu")

# Create model
model = DeepfakeClassifier(backbone="b4")

# Load trained weights
model_path = os.path.join("models", "best_model.pt")
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
    face_tensor must be a PyTorch tensor of shape [1, 3, 380, 380]
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