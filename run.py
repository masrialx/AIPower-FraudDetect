from flask import Flask, jsonify, request
import pandas as pd
import requests
import json

app = Flask(__name__)

# Load the CSV file once to use in multiple routes
df = pd.read_csv("fraud_data.csv")

# Google Gemini API endpoint and your API Key
GEMINI_API_KEY = 'your-google-gemini-api-key'  # Replace with your actual Gemini API Key
GEMINI_API_URL = 'https://gemini.googleapis.com/v1/analyze'  # Example URL (adjust as per actual API docs)

# Function to call Google Gemini API for transaction analysis
def analyze_transaction_with_gemini(transaction_data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GEMINI_API_KEY}'
    }
    payload = {
        'data': transaction_data
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response_data = response.json()
        
        if response.status_code == 200:
            return response_data
        else:
            return {"error": "Failed to analyze transaction", "details": response_data}
    except Exception as e:
        return {"error": str(e)}

# Flask Endpoint: Read fraud data and serve summary statistics
@app.route("/api/summary", methods=["GET"])
def summary():
    total_transactions = len(df)
    total_fraud_cases = df[df['fraud'] == 1].shape[0]
    fraud_percentage = (total_fraud_cases / total_transactions) * 100

    return jsonify({
        'total_transactions': total_transactions,
        'total_fraud_cases': total_fraud_cases,
        'fraud_percentage': fraud_percentage
    })

# Flask Endpoint: Serve fraud trends over time (line chart data)
@app.route("/api/fraud_trends", methods=["GET"])
def fraud_trends():
    fraud_over_time = df.groupby('date')['fraud'].sum().reset_index()
    return jsonify(fraud_over_time.to_dict(orient='records'))

# Flask Endpoint: Serve fraud cases by geographic location
@app.route("/api/fraud_geography", methods=["GET"])
def fraud_geography():
    fraud_by_location = df.groupby('location')['fraud'].sum().reset_index()
    return jsonify(fraud_by_location.to_dict(orient='records'))

# Flask Endpoint: Serve fraud cases by device/browser
@app.route("/api/fraud_device_browser", methods=["GET"])
def fraud_device_browser():
    fraud_by_device = df.groupby(['device', 'browser'])['fraud'].sum().reset_index()
    return jsonify(fraud_by_device.to_dict(orient='records'))

# Flask Endpoint: Analyze a single transaction using Google Gemini API
@app.route("/api/analyze_transaction", methods=["POST"])
def analyze_transaction():
    transaction_data = request.json  # Expecting JSON data in the request body

    if not transaction_data:
        return jsonify({"error": "No transaction data provided"}), 400
    
    # Call the Gemini API to analyze the transaction
    analysis_result = analyze_transaction_with_gemini(transaction_data)
    
    if 'error' in analysis_result:
        return jsonify(analysis_result), 500

    # Return the analysis result from Google Gemini API
    return jsonify(analysis_result), 200

if __name__ == "__main__":
    app.run(debug=True)

