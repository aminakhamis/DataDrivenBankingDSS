# Data-Driven Banking Decision Support System for Loan Approval

## Project Overview

This project is a machine learning-based Loan Approval Decision Support System.

The system predicts whether a customer's loan application will be **APPROVED** or **NOT APPROVED** based on financial, credit, employment, and education information.

## 🚀 Live System

👉 [Open Live System](https://datadrivenbankingdss-kdssd4wwhsvtbnieg6qqqv.streamlit.app/)

## Project Objectives

- Predict loan approval using machine learning.
- Provide approval probability.
- Store loan applications in a database.
- Provide dashboard statistics and charts.
- Search and filter customer applications.

## Machine Learning Model

The system uses a **Random Forest Classifier** for loan approval prediction.

The model achieved approximately **92.98% accuracy** on the test dataset.

## Input Features

- Annual Income
- Monthly Income
- Credit Score
- Loan Amount
- Loan Duration
- Total Debt to Income Ratio
- Interest Rate
- Base Interest Rate
- Monthly Loan Payment
- Total Assets
- Net Worth
- Age
- Experience
- Length of Credit History
- Employment Status
- Education Level

## System Features

- New Loan Application
- Loan Approval Prediction
- Approval Probability
- Database Storage
- Dashboard Statistics
- Data Visualization
- Customer Applications Table
- Search Applications
- Filter Applications

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- SQLite
- Joblib

## Project Structure

```text
DataDrivenBankingDSS/
│
├── dashboard/
│   └── app.py
│
├── src/
│   └── prediction.py
│
├── models/
│   └── loan_approval_model.pkl
│
├── database/
│   └── loan_database.db
│
├── requirements.txt
└── README.md
Installation

Install the required libraries:

pip install -r requirements.txt
Running the System

Run the Streamlit application:

python -m streamlit run dashboard/app.py

How the System Works
The user enters customer information.
The Random Forest model analyzes the information.
The system predicts the loan approval decision.
The system provides the approval probability.
The application and prediction result are saved in the database.
The dashboard displays statistics and charts.
Loan Approval Output

The system provides:

APPROVED
NOT APPROVED
Approval Probability
Dashboard

The dashboard displays:

Total Applications
Approved Loans
Not Approved Loans
Average Approval Probability
Loan Approval Distribution
Employment Status Analysis
Approval Probability Chart
Search and Filter

Users can search and filter applications by:

Application ID
Loan Status
Employment Status
Education Level
Model Performance

The Random Forest model achieved approximately 92.98% accuracy on the test dataset.

Conclusion

The Data-Driven Banking Decision Support System uses machine learning to support loan approval decisions.
Approval Probability Chart
Search and Filter

Users can search and filter applications by:

Application ID
Loan Status
Employment Status
Education Level
Model Performance

The Random Forest model achieved approximately 92.98% accuracy on the test dataset.

Conclusion

The Data-Driven Banking Decision Support System uses machine learning to support loan approval decisions.
