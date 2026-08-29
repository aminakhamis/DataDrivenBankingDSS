import pandas as pd
import joblib


# ==================================================
# LOAD TRAINED MODEL
# ==================================================

rf_model = joblib.load(
    "loan_approval_model.pkl"
)


# ==================================================
# PREPARE CUSTOMER DATA
# ==================================================

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
    length_of_credit_history,
    employment_status,
    education_level
):

    customer_data = {

        "AnnualIncome": annual_income,

        "MonthlyIncome": monthly_income,

        "CreditScore": credit_score,

        "LoanAmount": loan_amount,

        "LoanDuration": loan_duration,

        "TotalDebtToIncomeRatio":
            total_debt_to_income,

        "InterestRate": interest_rate,

        "BaseInterestRate":
            base_interest_rate,

        "MonthlyLoanPayment":
            monthly_payment,

        "TotalAssets": total_assets,

        "NetWorth": net_worth,

        "Age": age,

        "Experience": experience,

        "LengthOfCreditHistory":
            length_of_credit_history,


        # Employment
        "EmploymentStatus_Self-Employed":
            1 if employment_status == "Self-Employed" else 0,

        "EmploymentStatus_Unemployed":
            1 if employment_status == "Unemployed" else 0,


        # Education
        "EducationLevel_Bachelor":
            1 if education_level == "Bachelor" else 0,

        "EducationLevel_Doctorate":
            1 if education_level == "Doctorate" else 0,

        "EducationLevel_High School":
            1 if education_level == "High School" else 0,

        "EducationLevel_Master":
            1 if education_level == "Master" else 0
    }


    customer_df = pd.DataFrame(
        [customer_data]
    )

    return customer_df


# ==================================================
# PREDICT LOAN
# ==================================================

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
    length_of_credit_history,
    employment_status,
    education_level
):

    # Prepare customer data
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

        length_of_credit_history,

        employment_status,

        education_level
    )


    # Prediction
    prediction = rf_model.predict(
        customer_data
    )[0]


    # Probability
    probability = rf_model.predict_proba(
        customer_data
    )[0]


    # Approval probability
    approval_probability = probability[1] * 100


    # Decision
    if prediction == 1:

        decision = "APPROVED"

    else:

        decision = "NOT APPROVED"


    return decision, approval_probability


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    decision, probability = predict_loan(

        annual_income=60000,

        monthly_income=5000,

        credit_score=650,

        loan_amount=20000,

        loan_duration=24,

        total_debt_to_income=0.35,

        interest_rate=10,

        base_interest_rate=8,

        monthly_payment=950,

        total_assets=80000,

        net_worth=50000,

        age=30,

        experience=5,

        length_of_credit_history=6,

        employment_status="Employed",

        education_level="Bachelor"
    )


    print(
        "Loan Approval Prediction:",
        decision
    )

    print(
        "Approval Probability:",
        round(probability, 2),
        "%"
    )
