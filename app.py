"""
Project 4: Image or Text Recognition (Basic)
Industrial Training Kit | Batch 2026 — Powered by DecodeLabs
"""

import os
import cv2
import numpy as np
from flask import Flask, render_template, jsonify

app = Flask(__name__)
OUTPUT_DIR = "static"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_image():
    # 1. Create a blank canvas matrix (300x500 pixels, 3 channels)[cite: 1]
    canvas = np.zeros((300, 500, 3), dtype=np.uint8)
    canvas.fill(255) # White background

    # 2. Render text onto the image matrix[cite: 1]
    cv2.putText(canvas, "MASTERY ACHIEVED", (40, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # 3. Process grayscale transformation (stripping RGB color channels)[cite: 1]
    processed_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    # 4. Save output artifact[cite: 1]
    output_path = os.path.join(OUTPUT_DIR, "final_output.jpg")
    cv2.imwrite(output_path, processed_gray)

    return jsonify({"status": "success", "image_url": f"/{output_path}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
