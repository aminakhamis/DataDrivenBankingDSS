import pandas as pd
import joblib


# Load trained model
rf_model = joblib.load(
    "models/loan_approval_model.pkl"
)


def prepare_customer_data(
    annual_income,
    monthly_income,
    credit_score,
    loan_amount,
    loan_duration,
    total_debt_to_income,
    interest_rate,
    base_interest_rate,
    monthly_payment,
    total_assets,
    net_worth,
    age,
    experience,
    credit_history,
    employment_status,
    education_level
):

    customer = {
        "AnnualIncome": annual_income,
        "MonthlyIncome": monthly_income,
        "CreditScore": credit_score,
        "LoanAmount": loan_amount,
        "LoanDuration": loan_duration,
        "TotalDebtToIncomeRatio": total_debt_to_income,
        "InterestRate": interest_rate,
        "BaseInterestRate": base_interest_rate,
        "MonthlyLoanPayment": monthly_payment,
        "TotalAssets": total_assets,
        "NetWorth": net_worth,
        "Age": age,
        "Experience": experience,
        "LengthOfCreditHistory": credit_history,

        "EmploymentStatus_Self-Employed":
            1 if employment_status == "Self-Employed" else 0,

        "EmploymentStatus_Unemployed":
            1 if employment_status == "Unemployed" else 0,

        "EducationLevel_Bachelor":
            1 if education_level == "Bachelor" else 0,

        "EducationLevel_Doctorate":
            1 if education_level == "Doctorate" else 0,

        "EducationLevel_High School":
            1 if education_level == "High School" else 0,

        "EducationLevel_Master":
            1 if education_level == "Master" else 0
    }

    return pd.DataFrame([customer])


def predict_loan(
    annual_income,
    monthly_income,
    credit_score,
    loan_amount,
    loan_duration,
    total_debt_to_income,
    interest_rate,
    base_interest_rate,
    monthly_payment,
    total_assets,
    net_worth,
    age,
    experience,
    credit_history,
    employment_status,
    education_level
):

    customer_data = prepare_customer_data(
        annual_income,
        monthly_income,
        credit_score,
        loan_amount,
        loan_duration,
        total_debt_to_income,
        interest_rate,
        base_interest_rate,
        monthly_payment,
        total_assets,
        net_worth,
        age,
        experience,
        credit_history,
        employment_status,
        education_level
    )

    prediction = rf_model.predict(customer_data)

    probability = rf_model.predict_proba(customer_data)

    approval_probability = probability[0][1] * 100

    if prediction[0] == 1:
        decision = "APPROVED"
    else:
        decision = "NOT APPROVED"

    return decision, approval_probability