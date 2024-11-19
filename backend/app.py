from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from solver import solve_block_blast
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["*"]}})  # Allow CORS for all routes

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
        file_bytes = file.read()
        if not file_bytes:
            print("Empty file content")
            return jsonify({"error": "Empty file content"}), 400

        print("File read successfully, size: {} bytes".format(len(file_bytes)))

        image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)
        if image is None:
            print("Failed to read image")
            return jsonify({"error": "Failed to read image"}), 500

        print("Image decoded successfully")

        board_state = process_image(image)
        print("Image processed successfully: board_state shape = {}".format(board_state.shape))

        # Solve for the best moves
        best_moves = solve_block_blast(board_state)
        print("Solver executed successfully, moves: {}".format(best_moves))

        return jsonify({"moves": best_moves})

    except KeyError as e:
        print(f"KeyError occurred: {e}")
        return jsonify({"error": "KeyError: " + str(e)}), 400
    except ValueError as e:
        print(f"ValueError occurred: {e}")
        return jsonify({"error": "ValueError: " + str(e)}), 400
    except IOError as e:
        print(f"IOError occurred: {e}")
        return jsonify({"error": "IOError: " + str(e)}), 500
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return jsonify({"error": "Unexpected error: " + str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

def process_image(image):
    # Dummy function to simulate image processing
    # Replace this with real image processing logic
    print("Processing image (dummy function)")
    return np.zeros((10, 10))

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
