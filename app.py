from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load
import os

app = Flask(__name__)
CORS(app) 

# Load model
model = load('wildfire_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        new_data = pd.DataFrame({
            'Temperature': [data['Temperature'][0]],
            'Humidity': [data['Humidity'][0]],
            'Wind Speed': [data['Wind Speed'][0]],
            'Rainfall': [data['Rainfall'][0]]
        })
        predictions = model.predict(new_data)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
