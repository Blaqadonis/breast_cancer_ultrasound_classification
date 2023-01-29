import requests
from flask import Flask, request, jsonify
import numpy as np
#import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Loading the model
interpreter = tflite.Interpreter(model_path='cancer_model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
input_index = input_details[0]['index']
output_details = interpreter.get_output_details()
output_index = output_details[0]['index']

# Labels for the model's output
labels = [
    'Benign',
    'Malignant'
]

def predict_input(X):
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    # Getting the output of the model
    preds = interpreter.get_tensor(output_index)
    if preds[0][0] > preds[0][1]:
        return {"Prediction": 'Benign'}
    else:
        return {"Prediction": 'Malignant'}
   
    

def preprocess_input(x):
    x /= 127.5
    x -= 1.
    return x


@app.route('/predict', methods=['POST'])
def predict():
    # Getting the image URL from the request
    data = request.get_json()
    url = data.get('img_url')
    if not url:
        return jsonify(error="No 'img_url' parameter provided"), 400
    # Downloading the image
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((224, 224))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = preprocess_input(X)
    result = predict_input(X)
    # Returning the result as a JSON object
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)