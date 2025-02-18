from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file once to use in multiple routes
df = pd.read_csv("fraud_data.csv")

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

if __name__ == "__main__":
    app.run(debug=True)
