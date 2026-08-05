from app import app
from flask import request, jsonify
import os

# Folder where uploaded files will be stored
UPLOAD_FOLDER = "../uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -------------------------------
# Home API
# -------------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "AI Deepfake Detection Backend is Running"
    })


# -------------------------------
# Upload API
# -------------------------------
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


# -------------------------------
# Detect API
# -------------------------------
@app.route("/detect", methods=["POST"])
def detect():

    # Temporary response
    # Later this will be replaced with Olivia's AI model output

    result = {
        "status": "Fake",
        "confidence": 96,
        "voice": "Fake",
        "lip_sync": "Mismatch"
    }

    return jsonify(result)


# -------------------------------
# Complaint API
# -------------------------------
@app.route("/complaint", methods=["POST"])
def complaint():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    description = data.get("description")

    complaint = {
        "complaint_id": "CMP2026001",
        "name": name,
        "email": email,
        "phone": phone,
        "description": description,
        "status": "Complaint Submitted Successfully"
    }

    return jsonify(complaint)


# -------------------------------
# Report API
# -------------------------------
@app.route("/report", methods=["GET"])
def report():

    # Temporary report
    # Later this will be replaced by Tharshini's PDF generation module

    report = {
        "status": "Fake",
        "confidence": 96,
        "voice": "Fake",
        "lip_sync": "Mismatch",
        "generated_time": "05-08-2026 07:30 PM",
        "report": "Deepfake Analysis Report Generated Successfully"
    }

    return jsonify(report)