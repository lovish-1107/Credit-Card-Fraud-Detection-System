# Credit Card Fraud Detection System

## Overview

The Credit Card Fraud Detection System is a Machine Learning based desktop application developed using Python, Tkinter, SQLite, and Scikit-Learn. The system helps detect potentially fraudulent credit card transactions and provides transaction management, analytics, trend visualization, and report generation.

This project combines Machine Learning and Database Management to provide a practical fraud detection solution with an easy-to-use graphical user interface.

---

## Features

### User Management

* User Registration
* User Login Authentication
* Secure Access Control

### Fraud Detection

* Machine Learning Based Fraud Prediction
* Fraud Probability Score
* Legitimate/Fraud Classification

### Transaction Management

* Add New Transactions
* Store Transaction Details
* View Transaction History

### Analytics Dashboard

* Total Transactions
* Fraud Transactions
* Legitimate Transactions
* Fraud Rate Analysis
* Pie Chart Visualization
* Bar Chart Visualization

### Reports

* Export CSV Report
* Export Excel Report

### Trend Analysis

* Transaction Trend Analysis
* Fraud Trend Analysis
* Graphical Visualization using Matplotlib

### Administration

* View Registered Users
* Delete Users
* Monitor System Statistics

---

## Technology Stack

### Frontend

* Tkinter

### Backend

* Python

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* Logistic Regression
* Decision Tree

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib

### Model Storage

* Joblib

---

## Project Structure

```text
Credit-Card-Fraud-Detection-System
│
├── main.py
├── login.py
├── register.py
├── dashboard.py
├── add_transaction.py
├── predict.py
├── train_model.py
├── history.py
├── analytics.py
├── monthly_trend.py
├── export_csv.py
├── export_excel.py
├── admin_panel.py
│
├── fraud_model.pkl
├── database.db
│
├── dataset/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset Information

This project uses the Credit Card Fraud Detection Dataset from Kaggle.

Due to GitHub file size limitations, the dataset file is not included in this repository.

Download the dataset from:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

After downloading:

1. Create a folder named `dataset`
2. Place `creditcard.csv` inside the folder

Example:

```text
dataset/
└── creditcard.csv
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Credit-Card-Fraud-Detection-System.git
```

### Navigate to Project Folder

```bash
cd Credit-Card-Fraud-Detection-System
```

### Install Required Libraries

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install scikit-learn
pip install joblib
pip install openpyxl
```

Or:

```bash
pip install -r requirements.txt
```

---

## Train Machine Learning Model

Before running the project:

```bash
python train_model.py
```

This generates:

```text
fraud_model.pkl
```

---

## Run Project

```bash
python main.py
```

---

## Workflow

```text
Start Project
      ↓
Login/Register
      ↓
Dashboard
      ↓
Add Transaction
      ↓
Fraud Prediction
      ↓
Store in Database
      ↓
Analytics & Reports
```

---

## Future Enhancements

* Real-Time Fraud Detection
* Email Alert System
* OTP Verification
* Cloud Database Integration
* Deep Learning Models
* Web-Based Version
* Mobile Application Support

---

## Learning Outcomes

* Machine Learning Integration
* Python GUI Development
* Database Management
* Data Analysis
* Data Visualization
* Software Development Lifecycle

---

## Author

Lovish Dogra

B.Tech CSE (AI & ML)

Quantum University

---

## License

This project is licensed under the MIT License.
