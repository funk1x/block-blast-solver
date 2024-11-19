from flask import Flask, request, jsonify
import cv2
import numpy as np
from solver import solve_block_blast

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve():
    file = request.files['file']
    file.save('uploaded_image.png')

    # Process the image
    image = cv2.imread('uploaded_image.png')
    board_state = process_image(image)

    # Solve for the best moves
    best_moves = solve_block_blast(board_state)

    return jsonify({"moves": best_moves})

def process_image(image):
    # Dummy function to simulate image processing
    # Replace this with real image processing logic
    return np.zeros((10, 10))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
