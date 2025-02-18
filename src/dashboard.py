import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# Fetch the data from Flask API endpoints
def fetch_data(endpoint):
    response = requests.get(f"http://127.0.0.1:5000{endpoint}")
    return response.json()

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Fraud Insights Dashboard"),

    # Summary Section
    html.Div(id='summary-boxes'),

    # Line chart for fraud trends
    dcc.Graph(id='fraud-trends-chart'),

    # Map (Geography analysis)
    dcc.Graph(id='fraud-geography-chart'),

    # Bar chart for devices and browsers
    dcc.Graph(id='fraud-device-browser-chart')
])

# Callback for updating summary boxes
@app.callback(
    Output('summary-boxes', 'children'),
    Input('summary-boxes', 'id')  # Triggered once
)
def update_summary_boxes(_):
    data = fetch_data("/api/summary")
    return html.Div([
        html.Div(f"Total Transactions: {data['total_transactions']}"),
        html.Div(f"Total Fraud Cases: {data['total_fraud_cases']}"),
        html.Div(f"Fraud Percentage: {data['fraud_percentage']:.2f}%")
    ])

# Callback for updating fraud trends (line chart)
@app.callback(
    Output('fraud-trends-chart', 'figure'),
    Input('fraud-trends-chart', 'id')  # Triggered once
)
def update_fraud_trends(_):
    data = fetch_data("/api/fraud_trends")
    dates = [entry['date'] for entry in data]
    fraud_counts = [entry['fraud'] for entry in data]
    
    return {
        'data': [go.Scatter(x=dates, y=fraud_counts, mode='lines', name='Fraud Cases')],
        'layout': go.Layout(title="Fraud Cases Over Time", xaxis={'title': 'Date'}, yaxis={'title': 'Number of Fraud Cases'})
    }

# Callback for updating fraud geography (map)
@app.callback(
    Output('fraud-geography-chart', 'figure'),
    Input('fraud-geography-chart', 'id')  # Triggered once
)
def update_fraud_geography(_):
    data = fetch_data("/api/fraud_geography")
    locations = [entry['location'] for entry in data]
    fraud_counts = [entry['fraud'] for entry in data]
    
    return {
        'data': [go.Bar(x=locations, y=fraud_counts)],
        'layout': go.Layout(title="Fraud Cases by Location", xaxis={'title': 'Location'}, yaxis={'title': 'Number of Fraud Cases'})
    }

# Callback for updating fraud by device/browser (bar chart)
@app.callback(
    Output('fraud-device-browser-chart', 'figure'),
    Input('fraud-device-browser-chart', 'id')  # Triggered once
)
def update_fraud_device_browser(_):
    data = fetch_data("/api/fraud_device_browser")
    devices = [f"{entry['device']} - {entry['browser']}" for entry in data]
    fraud_counts = [entry['fraud'] for entry in data]
    
    return {
        'data': [go.Bar(x=devices, y=fraud_counts)],
        'layout': go.Layout(title="Fraud Cases by Device and Browser", xaxis={'title': 'Device/Browser'}, yaxis={'title': 'Number of Fraud Cases'})
    }

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
