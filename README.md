# Fraud Detection System – Adey Innovations Inc.

## 📌 Project Overview

This project builds a fraud detection system for e-commerce and credit card transactions for Adey Innovations Inc., a FinTech company.

Fraud detection is a high-impact machine learning problem where:
- False positives harm customer experience
- False negatives lead to financial loss

The objective is to build a robust ML pipeline that detects fraud using behavioral, temporal, and geolocation-based features.

The project uses:
- E-commerce transactions (Fraud_Data.csv)
- IP-to-country mapping (IpAddress_to_Country.csv)
- Credit card transactions (creditcard.csv)

---

## 📁 Project Structure

fraud-detection/
│
├── data/
│   ├── raw/                 # Original datasets
│   ├── processed/           # Cleaned and feature-engineered data
│
├── notebooks/               # Jupyter notebooks for analysis and modeling
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   ├── shap-explainability.ipynb
│
├── src/                     # Reusable Python code
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│
├── models/                  # Trained ML models (saved artifacts)
│   └── README.md
│
├── scripts/                # Automation scripts (future use)
│   └── README.md
│
├── tests/                  # Unit tests (optional)
│
├── requirements.txt
├── README.md
└── .gitignore
## 📊 Data Sources

### Fraud_Data.csv
E-commerce transaction dataset containing:
- user_id, device_id, browser, source
- signup_time, purchase_time
- purchase_value, ip_address
- target: class (1 = fraud, 0 = legitimate)

---

### IpAddress_to_Country.csv
Maps IP address ranges to countries for geolocation enrichment.

---

### creditcard.csv
Bank transaction dataset with anonymized PCA features (V1–V28).
- target: Class (1 = fraud, 0 = legitimate)

---

## ⚙️ Setup Instructions

### 1. Create virtual environment

python -m venv venv

---

### 2. Activate environment

Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

## ▶️ How to Run the Project

### Step 1: Run EDA

Open Jupyter Notebook:

jupyter notebook

Run:
- notebooks/eda-fraud-data.ipynb
- notebooks/eda-creditcard.ipynb

---

### Step 2: Run Feature Engineering

Run:
notebooks/feature-engineering.ipynb

This includes:
- Time-based features (hour, day, time_since_signup)
- User and device transaction frequency
- IP-to-country mapping
- Encoding categorical variables

---

### Step 3: Run Modeling (Task 2)

Run:
notebooks/modeling.ipynb

Includes:
- Train/test split
- SMOTE for class imbalance (training only)
- Logistic Regression baseline
- Random Forest / XGBoost models
- Evaluation using AUC-PR and F1-score

---

### Step 4: Run Explainability (Task 3)

Run:
notebooks/shap-explainability.ipynb

Includes:
- SHAP global feature importance
- Individual prediction explanations
- Business interpretation of model behavior

---

## 🔧 Feature Engineering Summary

Key features created:
- time_since_signup
- hour_of_day
- day_of_week
- user_transaction_count
- device_transaction_count
- country (from IP mapping)
- encoded categorical variables (browser, source, sex)

---

## 📦 Machine Learning Approach

Models used:
- Logistic Regression (baseline)
- Random Forest / XGBoost (ensemble)

Evaluation metrics:
- Precision
- Recall
- F1-score
- AUC-PR (primary metric due to imbalance)

---

## ⚖️ Class Imbalance Strategy

The dataset is highly imbalanced.

To handle this:
- SMOTE is applied ONLY on training data
- No resampling on test data
- Evaluation done on original distribution

---

## 📂 Folder Purpose

- data/ → raw and processed datasets
- notebooks/ → EDA, feature engineering, modeling
- src/ → reusable Python functions (cleaning + feature engineering)
- models/ → saved trained models
- scripts/ → automation tools (future use)
- tests/ → optional unit tests

---

## 🚀 Key Insights

- Fraud happens more often shortly after account creation
- Certain devices show repeated suspicious behavior
- Geographic regions show varying fraud rates
- Behavioral features are strong fraud indicators

---

## 👨‍💻 Author

Fraud Detection Project – Adey Innovations Inc.# fraud-detection
