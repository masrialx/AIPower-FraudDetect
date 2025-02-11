import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import socket
import struct
from sklearn.preprocessing import StandardScaler

# Load the datasets
fraud_data = pd.read_csv('../Data/Fraud_Data.csv')
ip_address_data = pd.read_csv('../Data/IpAddress_to_Country.csv')

# Step 1: Handle Missing Values
# Check for missing values
print("Missing values in Fraud Data:\n", fraud_data.isnull().sum())
print("\nMissing values in IP Address Data:\n", ip_address_data.isnull().sum())

# Handle missing values
fraud_data.fillna(fraud_data.mean(), inplace=True)  # Impute numerical columns with mean
fraud_data.dropna(subset=['some_critical_column'], inplace=True)  # Drop rows with missing critical column values

# Alternatively, we could drop rows with any missing values
# fraud_data.dropna(inplace=True)

# Verify no missing values after handling
print("\nMissing values after handling:\n", fraud_data.isnull().sum())

# Step 2: Data Cleaning
# Remove duplicate rows
fraud_data.drop_duplicates(inplace=True)

# Ensure correct data types for some columns (e.g., 'ip_address' should be a string, 'purchase_value' should be a float)
fraud_data['ip_address'] = fraud_data['ip_address'].astype(str)
fraud_data['purchase_value'] = fraud_data['purchase_value'].astype(float)

# Check the data types of all columns
print(fraud_data.dtypes)

# Step 3: Exploratory Data Analysis (EDA)

## 3.1 Univariate Analysis
# Visualize the distribution of 'purchase_value'
plt.figure(figsize=(10, 6))
sns.histplot(fraud_data['purchase_value'], kde=True, bins=30)
plt.title('Distribution of Purchase Value')
plt.show()

# Visualize the distribution of the target variable ('class') - 0: Non-Fraud, 1: Fraud
print(fraud_data['class'].value_counts())  # This will show the count of each class (fraud vs non-fraud)

## 3.2 Bivariate Analysis
# Correlation heatmap for numerical variables
plt.figure(figsize=(12, 8))
sns.heatmap(fraud_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Boxplot to visualize 'purchase_value' vs 'class'
plt.figure(figsize=(8, 6))
sns.boxplot(x='class', y='purchase_value', data=fraud_data)
plt.title('Purchase Value vs Fraud Class')
plt.show()

# Step 4: Merge Datasets for Geolocation Analysis

## 4.1 Convert IP Addresses to Integer Format
# Function to convert IP address to an integer
def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]

# Apply the conversion to 'ip_address' column
fraud_data['ip_address_int'] = fraud_data['ip_address'].apply(ip_to_int)

# Check the conversion
print(fraud_data[['ip_address', 'ip_address_int']].head())

## 4.2 Merge Fraud_Data with IpAddress_to_Country.csv
# Convert IP addresses to integer format in the IP address dataset
ip_address_data['ip_address_int'] = ip_address_data['ip_address'].apply(ip_to_int)

# Merge the fraud data with the IP address to country mapping based on the IP address integer
merged_data = pd.merge(fraud_data, ip_address_data, on='ip_address_int', how='left')

# Check the merged dataset
print(merged_data.head())

# Step 5: Feature Engineering

## 5.1 Transaction Frequency and Velocity
# Calculate transaction frequency for each user (assuming we have 'user_id' column)
transaction_freq = fraud_data.groupby('user_id')['purchase_value'].count().reset_index()
transaction_freq.rename(columns={'purchase_value': 'transaction_frequency'}, inplace=True)

# Merge this feature back to the main dataset
fraud_data = pd.merge(fraud_data, transaction_freq, on='user_id', how='left')

# Calculate transaction velocity (time difference between the first and last transaction for each user)
fraud_data['purchase_time'] = pd.to_datetime(fraud_data['purchase_time'])
user_velocity = fraud_data.groupby('user_id')['purchase_time'].max() - fraud_data.groupby('user_id')['purchase_time'].min()
fraud_data['transaction_velocity'] = user_velocity.dt.total_seconds()

# Inspect new features
print(fraud_data[['user_id', 'transaction_frequency', 'transaction_velocity']].head())

## 5.2 Time-Based Features
# Extract time-based features
fraud_data['hour_of_day'] = fraud_data['purchase_time'].dt.hour
fraud_data['day_of_week'] = fraud_data['purchase_time'].dt.dayofweek

# Check the result
print(fraud_data[['purchase_time', 'hour_of_day', 'day_of_week']].head())

# Step 6: Normalization and Scaling

## 6.1 Normalize or Scale Numerical Features
# Apply scaling to numerical features
scaler = StandardScaler()
fraud_data[['purchase_value', 'transaction_frequency', 'transaction_velocity']] = scaler.fit_transform(
    fraud_data[['purchase_value', 'transaction_frequency', 'transaction_velocity']]
)

# Check scaled features
print(fraud_data[['purchase_value', 'transaction_frequency', 'transaction_velocity']].head())

# Step 7: Encode Categorical Features

## 7.1 One-Hot Encoding for Categorical Features
# One-hot encode the 'country' feature (if applicable)
fraud_data = pd.get_dummies(fraud_data, columns=['country'], drop_first=True)

# Check the result
print(fraud_data.head())
