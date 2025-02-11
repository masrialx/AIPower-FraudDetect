# src/data_preprocessing.py
import ipaddress
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from datetime import datetime

# Load Fraud Data
fraud_data = pd.read_csv('../Data/Fraud_Data.csv')
print(fraud_data.head())

# Load Credit Card Data
creditcard_data = pd.read_csv('../Data/creditcard.csv')
print(creditcard_data.head())

# Check for missing values in both datasets
print(fraud_data.isnull().sum())
print(creditcard_data.isnull().sum())

# Optionally, handle missing values
fraud_data.fillna(method='ffill', inplace=True)  # Or use 'bfill' or dropna() depending on your data
creditcard_data.fillna(method='ffill', inplace=True)

# Remove duplicates if any
fraud_data.drop_duplicates(inplace=True)
creditcard_data.drop_duplicates(inplace=True)

# Convert 'purchase_time' to datetime format
fraud_data['purchase_time'] = pd.to_datetime(fraud_data['purchase_time'], errors='coerce')

# Check data types
print(fraud_data.dtypes)

# Plot histograms for numerical features
fraud_data.hist(figsize=(10, 10))
plt.show()

# Target variable distribution
sns.countplot(x='class', data=fraud_data)
plt.show()

# Exclude non-numeric columns for correlation
numeric_data = fraud_data.select_dtypes(include=[np.number])

# Plot correlation heatmap
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Visualizing relationships between features
sns.pairplot(fraud_data[['purchase_value', 'age', 'class']])
plt.show()

# Convert IP to integer
def ip_to_int(ip):
    try:
        # Only attempt conversion if the IP address is valid
        return int(ipaddress.IPv4Address(ip))
    except ValueError:
        # If invalid IP, return a placeholder value, e.g., NaN
        return np.nan

# Apply the conversion to the IP column
fraud_data['ip_address_int'] = fraud_data['ip_address'].apply(ip_to_int)
