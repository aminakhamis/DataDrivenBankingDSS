import streamlit as st
import sqlite3
import pandas as pd
from prediction import predict_loan


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Loan Approval System",
    page_icon="🏦",
    layout="wide"
)


# ==================================================
# DATABASE
# ==================================================

DATABASE_PATH = "loan_database.db"


def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loan_applications (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            annual_income REAL,
            monthly_income REAL,
            credit_score REAL,
            loan_amount REAL,
            loan_duration REAL,
            total_debt_to_income REAL,
            interest_rate REAL,
            base_interest_rate REAL,
            monthly_payment REAL,
            total_assets REAL,
            net_worth REAL,
            age REAL,
            experience REAL,
            credit_history REAL,

            employment_status TEXT,
            education_level TEXT,

            prediction TEXT,
            approval_probability REAL,

            application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_application(
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
    education_level,
    prediction,
    approval_probability
):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO loan_applications (
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
            education_level,
            prediction,
            approval_probability
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
        education_level,
        prediction,
        approval_probability
    ))

    connection.commit()
    connection.close()


def load_applications():

    connection = sqlite3.connect(DATABASE_PATH)

    data = pd.read_sql_query(
        """
        SELECT *
        FROM loan_applications
        ORDER BY id DESC
        """,
        connection
    )

    connection.close()

    return data


# Create database automatically
create_database()


# ==================================================
# TITLE
# ==================================================

st.title("🏦 Loan Approval Decision Support System")

st.write(
    "Welcome to the Loan Approval Prediction System"
)

st.divider()


# ==================================================
# CUSTOMER INFORMATION
# ==================================================

st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)


# ==================================================
# COLUMN 1
# ==================================================

with col1:

    annual_income = st.number_input(
        "Annual Income",
        min_value=0.0,
        value=60000.0
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0.0,
        value=5000.0
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=0.0,
        value=650.0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=20000.0
    )

    loan_duration = st.number_input(
        "Loan Duration",
        min_value=0.0,
        value=24.0
    )

    total_debt_to_income = st.number_input(
        "Total Debt to Income Ratio",
        min_value=0.0,
        value=0.35
    )

    interest_rate = st.number_input(
        "Interest Rate",
        min_value=0.0,
        value=10.0
    )


# ==================================================
# COLUMN 2
# ==================================================

with col2:

    base_interest_rate = st.number_input(
        "Base Interest Rate",
        min_value=0.0,
        value=8.0
    )

    monthly_payment = st.number_input(
        "Monthly Loan Payment",
        min_value=0.0,
        value=950.0
    )

    total_assets = st.number_input(
        "Total Assets",
        min_value=0.0,
        value=80000.0
    )

    net_worth = st.number_input(
        "Net Worth",
        min_value=0.0,
        value=50000.0
    )

    age = st.number_input(
        "Age",
        min_value=18.0,
        value=30.0
    )

    experience = st.number_input(
        "Experience",
        min_value=0.0,
        value=5.0
    )

    credit_history = st.number_input(
        "Length of Credit History",
        min_value=0.0,
        value=6.0
    )


# ==================================================
# EMPLOYMENT AND EDUCATION
# ==================================================

st.subheader("💼 Employment and Education")

col1, col2 = st.columns(2)


with col1:

    employment_status = st.selectbox(
        "Employment Status",
        [
            "Employed",
            "Self-Employed",
            "Unemployed"
        ]
    )


with col2:

    education_level = st.selectbox(
        "Education Level",
        [
            "Associate",
            "Bachelor",
            "High School",
            "Master",
            "Doctorate"
        ]
    )


st.divider()


# ==================================================
# PREDICTION
# ==================================================

if st.button(
    "🔍 Predict Loan",
    use_container_width=True
):

    try:

        # Machine Learning Prediction
        decision, probability = predict_loan(

            annual_income=annual_income,
            monthly_income=monthly_income,
            credit_score=credit_score,
            loan_amount=loan_amount,
            loan_duration=loan_duration,
            total_debt_to_income=total_debt_to_income,
            interest_rate=interest_rate,
            base_interest_rate=base_interest_rate,
            monthly_payment=monthly_payment,
            total_assets=total_assets,
            net_worth=net_worth,
            age=age,
            experience=experience,
            credit_history=credit_history,
            employment_status=employment_status,
            education_level=education_level
        )


        # Save application
        save_application(

            annual_income=annual_income,
            monthly_income=monthly_income,
            credit_score=credit_score,
            loan_amount=loan_amount,
            loan_duration=loan_duration,
            total_debt_to_income=total_debt_to_income,
            interest_rate=interest_rate,
            base_interest_rate=base_interest_rate,
            monthly_payment=monthly_payment,
            total_assets=total_assets,
            net_worth=net_worth,
            age=age,
            experience=experience,
            credit_history=credit_history,
            employment_status=employment_status,
            education_level=education_level,
            prediction=decision,
            approval_probability=probability
        )


        # Display result
        st.subheader("📊 Loan Approval Result")


        if decision == "APPROVED":

            st.success(
                "✅ Loan Approval Prediction: APPROVED"
            )

        else:

            st.error(
                "❌ Loan Approval Prediction: NOT APPROVED"
            )


        st.metric(
            "Approval Probability",
            f"{probability:.2f}%"
        )


        st.success(
            "Application saved successfully to database."
        )


    except Exception as error:

        st.error(
            f"Prediction Error: {error}"
        )


# ==================================================
# DASHBOARD OVERVIEW
# ==================================================

st.divider()

st.subheader("📊 Dashboard Overview")


applications = load_applications()


if applications.empty:

    st.info(
        "No loan applications available yet."
    )

else:

    total_applications = len(
        applications
    )

    approved_applications = len(
        applications[
            applications["prediction"] == "APPROVED"
        ]
    )

    not_approved_applications = len(
        applications[
            applications["prediction"] == "NOT APPROVED"
        ]
    )

    average_probability = applications[
        "approval_probability"
    ].mean()


    # Statistics cards

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Total Applications",
            total_applications
        )


    with col2:

        st.metric(
            "Approved Loans",
            approved_applications
        )


    with col3:

        st.metric(
            "Not Approved",
            not_approved_applications
        )


    with col4:

        st.metric(
            "Average Approval Probability",
            f"{average_probability:.2f}%"
        )


# ==================================================
# CHARTS
# ==================================================

if not applications.empty:

    st.divider()

    st.subheader(
        "📈 Loan Application Analysis"
    )


    chart_col1, chart_col2 = st.columns(2)


    # Approval Distribution

    with chart_col1:

        st.write(
            "### Loan Approval Distribution"
        )

        approval_counts = applications[
            "prediction"
        ].value_counts()

        st.bar_chart(
            approval_counts
        )


    # Employment Status

    with chart_col2:

        st.write(
            "### Applications by Employment Status"
        )

        employment_counts = applications[
            "employment_status"
        ].value_counts()

        st.bar_chart(
            employment_counts
        )


    # Approval Probability

    st.write(
        "### Approval Probability"
    )

    probability_data = applications[
        ["id", "approval_probability"]
    ].set_index("id")

    st.line_chart(
        probability_data
    )


# ==================================================
# CUSTOMER APPLICATIONS
# SEARCH & FILTER
# ==================================================

st.divider()

st.subheader(
    "📋 Customer Applications"
)


if applications.empty:

    st.info(
        "No customer applications found."
    )

else:

    st.subheader(
        "🔍 Search & Filter Applications"
    )


    # --------------------------------------------------
    # SEARCH AND FILTER CONTROLS
    # --------------------------------------------------

    col1, col2, col3 = st.columns(3)


    # Search by ID

    with col1:

        search_id = st.text_input(
            "Search by Application ID"
        )


    # Loan Status

    with col2:

        status_filter = st.selectbox(
            "Loan Status",
            [
                "All",
                "APPROVED",
                "NOT APPROVED"
            ]
        )


    # Employment Status

    with col3:

        employment_filter = st.selectbox(
            "Employment Status",
            [
                "All",
                "Employed",
                "Self-Employed",
                "Unemployed"
            ]
        )


    # Education Level

    education_filter = st.selectbox(
        "Education Level",
        [
            "All",
            "Associate",
            "Bachelor",
            "High School",
            "Master",
            "Doctorate"
        ]
    )


    # --------------------------------------------------
    # APPLY FILTERS
    # --------------------------------------------------

    filtered_applications = applications.copy()


    # Search by ID

    if search_id:

        filtered_applications = filtered_applications[
            filtered_applications["id"]
            .astype(str)
            .str.contains(
                search_id,
                case=False,
                na=False
            )
        ]


    # Loan Status

    if status_filter != "All":

        filtered_applications = filtered_applications[
            filtered_applications["prediction"]
            == status_filter
        ]


    # Employment Status

    if employment_filter != "All":

        filtered_applications = filtered_applications[
            filtered_applications[
                "employment_status"
            ] == employment_filter
        ]


    # Education Level

    if education_filter != "All":

        filtered_applications = filtered_applications[
            filtered_applications[
                "education_level"
            ] == education_filter
        ]


    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    st.write(
        f"Showing **{len(filtered_applications)}** application(s)"
    )


    st.dataframe(
        filtered_applications,
        use_container_width=True
    )
