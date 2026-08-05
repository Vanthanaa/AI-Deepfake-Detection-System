from app import app
from flask import request, jsonify
import os

# Folder where uploaded files will be stored
UPLOAD_FOLDER = "../uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return jsonify({
        "message": "AI Deepfake Detection Backend is Running"
    })

@app.route("/upload", methods=["POST"])
def upload_file():

    # Check if a file was sent
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Check if a file was selected
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Save the uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": file.filename
    })
@app.route("/detect", methods=["POST"])
def detect():

    result = {
        "status": "Fake",
        "confidence": 96,
        "voice": "Fake",
        "lip_sync": "Mismatch"
    }

    return jsonify(result)