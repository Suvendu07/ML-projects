import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Approval Prediction App")
st.markdown("Enter applicant details to predict loan status (Approved or Not Approved)")

# Input Fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self-Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode inputs
gender_val = 1 if gender == "Male" else 0
married_val = 1 if married == "Yes" else 0
dependents_val = 3 if dependents == "3+" else int(dependents)
education_val = 1 if education == "Graduate" else 0
self_employed_val = 1 if self_employed == "Yes" else 0
property_map = {"Urban": 2, "Semiurban": 1, "Rural": 0}
property_area_val = property_map[property_area]

# Combine into input array
input_data = np.array([[gender_val, married_val, dependents_val, education_val,
                        self_employed_val, applicant_income, coapplicant_income,
                        loan_amount, loan_amount_term, credit_history, property_area_val]])

# Predict
if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)[0]
    result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"
    st.success(f"Prediction: {result}")
