from flask import Flask, request, jsonify
import pickle
import pandas as pd
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the trained fraud detection model
with open('fraud_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Make prediction
        prediction = model.predict(df)
        
        # Log request and prediction
        logging.info(f"Prediction request: {data}")
        logging.info(f"Prediction result: {prediction.tolist()}")
        
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
