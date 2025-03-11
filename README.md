# **AI-Powered Fraud Detection System using Google Gemini API**

## **Overview**

This project implements an **AI-powered fraud detection system** using the **Google Gemini API**. The system detects and prevents fraudulent transactions in real-time by analyzing multimodal data such as transaction details, user behavior, and images attached to the transaction. It aims to provide scalable and adaptive fraud detection, offering an enhanced level of security for financial institutions and e-commerce platforms.

---

## **Table of Contents**

1. [Installation](#installation)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Usage](#usage)
5. [API Integration](#api-integration)
6. [Model Evaluation](#model-evaluation)
7. [Security and Compliance](#security-and-compliance)
8. [Contributing](#contributing)
9. [License](#license)

---

## **Installation**

Follow the steps below to set up the fraud detection system on your local machine or server.

### 1. Clone the repository:

```bash
git clone https://github.com/masrialx/AIPower-FraudDetect.git
cd AIPower-FraudDetect
```

### 2. Install required dependencies:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries for the project, including Google Gemini API SDK, machine learning libraries (such as TensorFlow, scikit-learn), and other dependencies.

---

## **Prerequisites**

Before you begin, ensure the following requirements are met:

1. **Google Gemini API Key**: You need a valid **API key** for accessing Google Gemini services. If you do not have one, you can obtain it from the [Google Cloud Console](https://console.cloud.google.com/).
   
2. **Python 3.x**: This project uses Python 3.8 or higher.
   
3. **Google Cloud SDK** (Optional for deployment): If you're deploying the system to Google Cloud, ensure that you have the Google Cloud SDK installed.

4. **Jupyter Notebook** (Optional for model training & evaluation): Install Jupyter to run the notebooks for training and evaluation.

---

## **Setup**

### 1. **Set Up Google Gemini API**

- Visit [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or use an existing one.
- Enable the **Google Gemini API**.
- Obtain your **API key** and save it for later use.

### 2. **Set Up Environment Variables**

You will need to configure your environment to securely store your **Google API Key**:

```bash
export GEMINI_API_KEY="your-api-key"
```

Alternatively, create a `.env` file in the project root with the following content:

```env
GEMINI_API_KEY=your-api-key
```

---

## **Usage**

### 1. **Run the Fraud Detection System**

The core of the fraud detection system is encapsulated in a Python script that integrates with the Google Gemini API. You can run the detection system with the following command:

```bash
python detect_fraud.py
```

This script will process a sample transaction and flag it as either **fraudulent** or **legitimate** based on the AI-powered analysis provided by Gemini.

### 2. **API Call Example**

To run the fraud detection for a single transaction, use the `detect_transaction` function:

```python
from fraud_detection import detect_transaction

transaction_data = {
    "user_id": "12345",
    "amount": 500,
    "location": "New York",
    "ip_address": "192.168.1.1",
    "transaction_notes": "Purchase of electronics"
}

result = detect_transaction(transaction_data)
print(result)
```

### 3. **Running the Fraud Detection System in Real-Time**

For real-time fraud detection, set up the system to monitor ongoing transactions via the API. You can integrate it with e-commerce platforms or banking systems. 

### 4. **Evaluate the Model**

To evaluate the performance of the fraud detection model, use the following Jupyter notebook:

```bash
jupyter notebook evaluate_model.ipynb
```

This notebook runs through the metrics like **accuracy**, **precision**, **recall**, and **F1-score** to assess the model's performance.

---

## **API Integration**

### 1. **Setting Up the Fraud Detection API**

The fraud detection system exposes an API endpoint that can be integrated into external platforms:

#### **Endpoint: `/api/v1/detect_fraud`**

- **Method**: POST
- **Request Body**: JSON object containing transaction details:
  
```json
{
  "user_id": "12345",
  "amount": 500,
  "location": "New York",
  "ip_address": "192.168.1.1",
  "transaction_notes": "Purchase of electronics"
}
```

- **Response**: JSON object with the fraud score and flag.

```json
{
  "fraud_score": 0.85,
  "status": "fraudulent",
  "message": "Transaction flagged as fraudulent due to unusual location and IP address"
}
```

### 2. **API Authentication**

To ensure secure API access, authenticate each request using **API tokens** or **OAuth 2.0**. The authentication procedure is defined in the API docs.

---

## **Model Evaluation**

Evaluate the fraud detection model using various **performance metrics**:

- **Accuracy**: Percentage of correctly predicted transactions (both legitimate and fraudulent).
- **Precision**: The ratio of true positive fraud cases detected to all instances flagged as fraud.
- **Recall**: The ratio of true positive fraud cases detected to all actual fraud cases.
- **F1-score**: The harmonic mean of precision and recall.

Run the evaluation with:

```bash
python evaluate_model.py
```

---

## **Security and Compliance**

### 1. **Data Encryption**
All sensitive data (e.g., transaction data) is encrypted using **AES-256** encryption to ensure security.

### 2. **Regulatory Compliance**
Ensure compliance with data protection laws like **GDPR** and **PCI-DSS** for handling user data and transactions.

---

## **Contributing**

We welcome contributions to the **AI-Powered Fraud Detection System**!

### **How to Contribute:**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

For large changes or feature suggestions, please open an issue first to discuss what you would like to change.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Additional Information**

- **Google Gemini Documentation**: [Google Gemini API Docs](https://cloud.google.com/gemini)
- **Machine Learning Libraries**: TensorFlow, scikit-learn

