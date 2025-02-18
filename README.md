# **Fraud Detection and Insights Dashboard**
## **Overview**
This project is aimed at improving fraud detection for both e-commerce transactions and bank credit transactions. The system leverages advanced machine learning models, geolocation analysis, and transaction pattern recognition to detect fraudulent activities. The project includes various tasks such as data analysis, model building, model explainability, and deployment.

An interactive **dashboard** is developed using **Flask** and **Dash** to visualize fraud insights, making it easy to track fraud trends, analyze transaction patterns, and visualize fraud across devices, browsers, and geographical locations.

## **Business Need**
Fraud detection plays a crucial role in securing transactions in the financial sector. By improving the accuracy of fraud detection, Adey Innovations Inc. can prevent financial losses, build trust with customers, and enhance the real-time monitoring of financial activities.

## **Tech Stack**
- **Backend:** Flask (for API development)
- **Frontend:** Dash (for interactive visualizations)
- **Machine Learning Libraries:** Scikit-learn, TensorFlow, Keras
- **Data Processing:** Pandas, Numpy
- **Data Visualization:** Plotly (for Dash)
- **Geolocation Analysis:** IP address to country mapping
- **Containerization:** Docker

## **Learning Outcomes**
- Building and deploying machine learning models using Flask.
- Containerizing applications using Docker.
- Creating REST APIs for machine learning models.
- Real-time prediction serving and model monitoring.
- Feature engineering and data preprocessing for fraud detection.
- Understanding and applying model explainability techniques like SHAP and LIME.
- Developing interactive dashboards for business insights.

## **Datasets**
- **Fraud_Data.csv:** E-commerce transaction data with fraud labels.
  - `user_id`, `signup_time`, `purchase_time`, `purchase_value`, `device_id`, `browser`, `sex`, `age`, `ip_address`, `class`
- **IpAddress_to_Country.csv:** Maps IP addresses to countries.
  - `lower_bound_ip_address`, `upper_bound_ip_address`, `country`
- **creditcard.csv:** Bank transaction data, anonymized for fraud detection.
  - `Time`, `V1 - V28`, `Amount`, `Class`

## **Features**
### **Task 1: Data Analysis and Preprocessing**
- Handle missing values and clean the data.
- Exploratory Data Analysis (EDA) for univariate and bivariate analysis.
- Merge datasets for geolocation analysis.
- Feature engineering for time-based and transaction velocity features.
- Normalize and scale data, and encode categorical features.

### **Task 2: Model Building and Training**
- Prepare data and separate features and targets.
- Split data into training and testing sets.
- Train various models like Logistic Regression, Random Forest, Gradient Boosting, MLP, CNN, RNN, and LSTM.
- Use **MLflow** for versioning and experiment tracking.

### **Task 3: Model Explainability**
- Use **SHAP** and **LIME** for model interpretability.
- SHAP and LIME plots to visualize feature importance and explain individual predictions.

### **Task 4: Model Deployment and API Development**
- Set up Flask API to serve trained models.
- Dockerize the Flask application for portability.
- Expose endpoints for fraud prediction and monitoring.
- Integrate Flask-Logging for real-time logging and monitoring.

### **Task 5: Build a Dashboard with Flask and Dash**
- Develop an interactive **Dash** dashboard to visualize fraud insights.
- Flask backend serves data from **Fraud_Data.csv** for the frontend visualization.
- Insights include:
  - Total transactions, fraud cases, and fraud percentages in summary boxes.
  - Line chart showing fraud cases over time.
  - Geographical fraud analysis with bar charts.
  - Fraud cases comparison across devices and browsers.

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/fraud-detection-dashboard.git
cd fraud-detection-dashboard
```

### **2. Create Virtual Environment and Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

Install required packages:
```bash
pip install -r requirements.txt
```

### **3. Running the Flask API**
Run the Flask API to serve the fraud detection models:
```bash
python app.py
```
The Flask server will be available at `http://127.0.0.1:5000/`.

### **4. Running the Dash Dashboard**
In another terminal, run the Dash app:
```bash
python dashboard.py
```
The Dash dashboard will be available at `http://127.0.0.1:8050/`.

## **API Endpoints**
- `/api/summary`: Get total transactions, fraud cases, and fraud percentages.
- `/api/fraud_trends`: Get fraud cases over time.
- `/api/fraud_geography`: Get fraud distribution by geography.
- `/api/fraud_device_browser`: Get fraud cases across devices and browsers.

## **Project Structure**
```
fraud-detection-dashboard/
├── app.py               # Flask backend
├── dashboard.py         # Dash frontend
├── fraud_data.csv       # E-commerce transaction data
├── ipaddress_to_country.csv  # IP address to country mapping
├── creditcard.csv       # Bank transaction data
├── requirements.txt     # List of dependencies
├── mlflow_tracking/     # Folder for MLflow experiment tracking
└── README.md            # Project documentation
```

## **Docker Setup**

### **1. Build Docker Image**
```bash
docker build -t fraud-detection-model .
```

### **2. Run Docker Container**
```bash
docker run -p 5000:5000 fraud-detection-model
```

## **Future Work**
- Real-time fraud detection and monitoring system.
- Model retraining and performance monitoring.
- Integration with larger e-commerce and banking platforms for production deployment.

