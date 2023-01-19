from flask import Flask, request, jsonify
import requests
import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras.preprocessing.image import load_img
import PIL.Image
from tensorflow.keras.utils import load_img
import numpy as np
import tflite_runtime.interpreter as tflite
 

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
    score = dict(zip(labels, preds[0]))
    print("Prediction: {}.".format(labels[np.argmax(score)]))
    return labels[np.argmax(score)]


@app.route('/predict', methods=['POST'])
def predict():
    # Getting the image URL from the JSON payload
    img_url = request.get_json()['url']
    # Downloading the image
    response = requests.get(img_url).content
    with open('img.jpg', 'wb') as handler:
        handler.write(response)
    img = load_img('img.jpg', target_size=(224, 224, 3))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = tflite.keras.applications.xception.preprocess_input(X)
    result = predict_input(X)
    # Returning the result as a JSON object
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)