# Data-Driven Banking Decision Support System for Loan Approval

## Project Overview

The Data-Driven Banking Decision Support System for Loan Approval is a machine learning-based system designed to support loan approval decisions.

The system analyzes customer financial, credit, employment, and education information and predicts whether a loan application is likely to be approved or not approved.

The system is designed to help make loan assessment faster, more consistent, and data-driven.

## Project Objectives

The main objectives of this project are:

- To develop a machine learning model for loan approval prediction.
- To predict whether a customer's loan application will be approved or not approved.
- To provide an approval probability for each application.
- To store customer loan applications and prediction results in a database.
- To provide dashboard statistics and data visualization.
- To provide search and filtering of customer applications.

## Machine Learning Model

The system uses the Random Forest Classifier for loan approval prediction.

Random Forest was selected because it can handle different types of customer features and can capture complex relationships between financial and credit-related variables.

The model achieved an accuracy of approximately 92.98% on the test dataset.

## Input Features

The system uses the following customer information:

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

The system provides the following features:

- New Loan Application
- Customer Information Input
- Automatic Encoding of Categorical Data
- Random Forest Prediction
- Loan Approval Decision
- Approval Probability
- Save Application to Database
- Dashboard Statistics
- Loan Approval Charts
- Employment Status Analysis
- Approval Probability Analysis
- Customer Applications Table
- Search Applications by ID
- Filter Applications by Loan Status
- Filter Applications by Employment Status
- Filter Applications by Education Level

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

First, make sure Python is installed on your computer.

Install the required libraries using:

pip install -r requirements.txt
Running the System

Run the Streamlit application using:

python -m streamlit run dashboard/app.py

After running the command, the system will open in a web browser.

How the System Works

The user enters customer financial, credit, employment, and education information.

The system sends the entered information to the trained Random Forest model.

The model processes the information and produces:

Loan approval decision.
Approval probability.

The application and prediction result are then saved in the SQLite database.

The dashboard displays statistics, charts, and previously submitted customer applications.

Loan Approval Output

The system provides two main prediction outcomes:

APPROVED
NOT APPROVED

It also displays the approval probability as a percentage.

Database

The system uses SQLite to store loan application information.

The database stores customer information together with the prediction result and approval probability.

Dashboard

The dashboard provides an overview of loan applications, including:

Total Applications
Approved Loans
Not Approved Loans
Average Approval Probability

It also provides charts for loan approval distribution, employment status, and approval probability.

Search and Filter

The Customer Applications section allows users to search and filter applications.

Users can:

Search by Application ID.
Filter by Loan Status.
Filter by Employment Status.
Filter by Education Level.

This makes it easier to find and analyze specific customer applications.

Model Performance

The Random Forest model achieved approximately 92.98% accuracy on the test dataset.

The model was trained using customer financial and demographic features and evaluated using a separate test dataset.

Conclusion

The Data-Driven Banking Decision Support System demonstrates how machine learning can be applied to support banking loan approval decisions.

The system combines machine learning, database storage, data visualization, and an interactive web dashboard to provide a complete loan approval decision support solution.

Installation
First, make sure Python is installed on your computer.
Install the required libraries using:
pip install -r requirements.txt
Running the System
Run the Streamlit application using:
python -m streamlit run dashboard/app.py
After running the command, the system will open in a web browser.
How the System Works
The user enters customer financial, credit, employment, and education information.
The system sends the entered information to the trained Random Forest model.
The model processes the information and produces:
Loan approval decision.
Approval probability.
The application and prediction result are then saved in the SQLite database.
The dashboard displays statistics, charts, and previously submitted customer applications.
Loan Approval Output
The system provides two main prediction outcomes:
APPROVED
NOT APPROVED
It also displays the approval probability as a percentage.
Database
The system uses SQLite to store loan application information.
The database stores customer information together with the prediction result and approval probability.
Dashboard
The dashboard provides an overview of loan applications, including:
Total Applications
Approved Loans
Not Approved Loans
Average Approval Probability
It also provides charts for loan approval distribution, employment status, and approval probability.
Search and Filter
The Customer Applications section allows users to search and filter applications.
Users can:
Search by Application ID.
Filter by Loan Status.
Filter by Employment Status.
Filter by Education Level.
This makes it easier to find and analyze specific customer applications.
Model Performance
The Random Forest model achieved approximately 92.98% accuracy on the test dataset.
The model was trained using customer financial and demographic features and evaluated using a separate test dataset.
Conclusion
The Data-Driven Banking Decision Support System demonstrates how machine learning can be applied to support banking loan approval decisions.
The system combines machine learning, database storage, data visualization, and an interactive web dashboard to provide a complete loan approval decision support solution.


Maelz hy nisieke

Ndiyo 👍 Kama unataka maelezo mafupi na rahisi, unaweza kuyaweka hivi kwenye README.md:

## Installation

Install the required libraries:

pip install -r requirements.txt

## Running the System

Run the application using:

python -m streamlit run dashboard/app.py

## How the System Works

The user enters customer information. The Random Forest model analyzes the information and predicts whether the loan will be approved or not.

The system also provides the approval probability and saves the application in the database.

## Loan Approval Output

The system provides:

- APPROVED
- NOT APPROVED
- Approval Probability

## Database

The system uses SQLite to store customer loan applications and prediction results.

## Dashboard

The dashboard displays:

- Total Applications
- Approved Loans
- Not Approved Loans
- Average Approval Probability
- Charts

## Search and Filter

Users can:

- Search applications by ID.
- Filter by loan status.
- Filter by employment status.
- Filter by education level.

## Model Performance

The Random Forest model achieved approximately **92.98% accuracy** on the test dataset.

## Conclusion

The system uses machine learning to support loan approval decisions. It combines prediction, database storage, dashboard statistics, charts, search, and filtering in one system.
Umenip maelz y kwanz ni y copy n hy vip maelz sahh ni yap hem nip yote kwa pamoja 

Sawa 👍 Hapa chini nimekuwekea README yote kuanzia mwanzo hadi mwisho, ikiwa na maelezo mafupi, rahisi, na yaliyopangwa vizuri. Copy yote kwa pamoja uiweke kwenye README.md.

# Data-Driven Banking Decision Support System for Loan Approval

## Project Overview

This project is a machine learning-based Loan Approval Decision Support System.

The system predicts whether a customer's loan application will be approved or not approved based on financial, credit, employment, and education information.

## Project Objectives

- To predict loan approval using machine learning.
- To provide approval probability.
- To store loan applications in a database.
- To provide dashboard statistics and charts.
- To allow users to search and filter applications.

## Machine Learning Model

The system uses a **Random Forest Classifier** for loan approval prediction.

The Random Forest model was selected because it can handle different customer features and identify complex relationships in the data.

The model achieved approximately **92.98% accuracy** on the test dataset.

## Input Features

The system uses the following customer information:

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
- Automatic Encoding
- Random Forest Prediction
- Approval Probability
- Save Application to Database
- Dashboard Statistics
- Charts
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

Run the Streamlit application using:

python -m streamlit run dashboard/app.py

The system will open in a web browser.

How the System Works

The user enters customer financial, credit, employment, and education information.

The system sends the information to the trained Random Forest model.

The model predicts whether the loan will be approved or not approved and provides the approval probability.

The application and prediction result are saved in the SQLite database.

Loan Approval Output

The system provides:

APPROVED
NOT APPROVED
Approval Probability
Database

The system uses SQLite to store customer loan applications and prediction results.

Dashboard

The dashboard displays:

Total Applications
Approved Loans
Not Approved Loans
Average Approval Probability
Loan Approval Distribution
Applications by Employment Status
Approval Probability Chart
Search and Filter

Users can search and filter customer applications by:

Application ID
Loan Status
Employment Status
Education Level
Model Performance

The Random Forest model achieved approximately 92.98% accuracy on the test dataset.

Conclusion

The Data-Driven Banking Decision Support System uses machine learning to support loan approval decisions.

The system combines loan prediction, approval probability, database storage, dashboard statistics, charts, search, and filtering in one application.


