import pandas as pd
import numpy as np
import shap
import lime
import lime.lime_tabular
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
fraud_data = pd.read_csv('Fraud_Data.csv')
creditcard_data = pd.read_csv('creditcard.csv')

# Preprocessing
fraud_data.fillna(method='ffill', inplace=True)
creditcard_data.fillna(method='ffill', inplace=True)

# Feature and Target Separation
X_fraud = fraud_data.drop(columns=['class'])
y_fraud = fraud_data['class']
X_credit = creditcard_data.drop(columns=['Class'])
y_credit = creditcard_data['Class']

# Train-Test Split
X_train_fraud, X_test_fraud, y_train_fraud, y_test_fraud = train_test_split(X_fraud, y_fraud, test_size=0.2, random_state=42)
X_train_credit, X_test_credit, y_train_credit, y_test_credit = train_test_split(X_credit, y_credit, test_size=0.2, random_state=42)

# Model Training
model_fraud = RandomForestClassifier(n_estimators=100, random_state=42)
model_fraud.fit(X_train_fraud, y_train_fraud)

model_credit = RandomForestClassifier(n_estimators=100, random_state=42)
model_credit.fit(X_train_credit, y_train_credit)

# Model Evaluation
y_pred_fraud = model_fraud.predict(X_test_fraud)
y_pred_credit = model_credit.predict(X_test_credit)

print("Fraud Detection Model Report:")
print(classification_report(y_test_fraud, y_pred_fraud))
print("Accuracy:", accuracy_score(y_test_fraud, y_pred_fraud))

print("Credit Card Fraud Detection Model Report:")
print(classification_report(y_test_credit, y_pred_credit))
print("Accuracy:", accuracy_score(y_test_credit, y_pred_credit))

# SHAP Explainability
explainer_fraud = shap.TreeExplainer(model_fraud)
shap_values_fraud = explainer_fraud.shap_values(X_test_fraud)
shap.summary_plot(shap_values_fraud[1], X_test_fraud)

explainer_credit = shap.TreeExplainer(model_credit)
shap_values_credit = explainer_credit.shap_values(X_test_credit)
shap.summary_plot(shap_values_credit[1], X_test_credit)

# SHAP Force Plot for a Single Prediction
shap.initjs()
idx = 0  # Index of the test instance to explain
shap.force_plot(explainer_fraud.expected_value[1], shap_values_fraud[1][idx], X_test_fraud.iloc[idx, :])

# SHAP Dependence Plot
shap.dependence_plot("V1", shap_values_fraud[1], X_test_fraud)

# LIME Explainability
explainer = lime.lime_tabular.LimeTabularExplainer(X_train_fraud.values, feature_names=X_train_fraud.columns, class_names=['Not Fraud', 'Fraud'], discretize_continuous=True)

exp = explainer.explain_instance(X_test_fraud.values[idx], model_fraud.predict_proba, num_features=10)
exp.show_in_notebook()

# LIME Feature Importance Plot
fig = exp.as_pyplot_figure()
plt.show()
