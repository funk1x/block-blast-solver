from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from solver import solve_block_blast
import io

app = Flask(__name__)
CORS(app, resources={r"/solve": {"origins": "*"}})  # Allow CORS for the /solve route

@app.route('/solve', methods=['POST'])
def solve():
    print("Solve function called")  # Debug print to confirm the route is being accessed
    try:
        # Check if a file was sent in the request
        if 'file' not in request.files:
            print("No file part in request")
            return jsonify({"error": "No file part in request"}), 400

        file = request.files['file']
        
        # Check if a file is actually selected
        if file.filename == '':
            print("No file selected")
            return jsonify({"error": "No file selected"}), 400

        # Read the uploaded file into memory
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        if image is None:
            print("Failed to read image")
            return jsonify({"error": "Failed to read image"}), 500

        print("File read successfully")

        board_state = process_image(image)
        print("Image processed successfully")

        # Solve for the best moves
        best_moves = solve_block_blast(board_state)
        print("Solver executed successfully")

        return jsonify({"moves": best_moves})

    except (KeyError, ValueError, IOError) as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

def process_image(image):
    # Dummy function to simulate image processing
    # Replace this with real image processing logic
    print("Processing image (dummy function)")
    return np.zeros((10, 10))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
