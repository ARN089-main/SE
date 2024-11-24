from flask import Flask, request, jsonify
from stegano import lsb
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/hide', methods=['POST'])
def hide():
    if 'image' not in request.files or 'text' not in request.form:
        return jsonify({'message': 'Missing image or text'}), 400

    image = request.files['image']
    text = request.form['text']

    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    output_path = os.path.join(UPLOAD_FOLDER, f'hidden_{filename}')
    hidden_img = lsb.hide(image_path, text)
    hidden_img.save(output_path)

    return jsonify({'message': f'Text hidden successfully in {output_path}'}), 200

@app.route('/reveal', methods=['POST'])
def reveal():
    if 'image' not in request.files:
        return jsonify({'message': 'Missing image'}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    try:
        hidden_text = lsb.reveal(image_path)
        return jsonify({'text': hidden_text}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to reveal text', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
