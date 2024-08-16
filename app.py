from flask import Flask, request, jsonify, render_template
import easyocr
import os

app = Flask(__name__)
reader = easyocr.Reader(['en'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file temporarily
    filepath = 'temp.jpg'
    file.save(filepath)

    # Perform OCR
    results = reader.readtext(filepath)
    os.remove(filepath)  # Clean up

    text = ' '.join([result[1] for result in results])
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
