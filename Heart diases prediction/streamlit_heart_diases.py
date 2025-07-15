import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"D:\ML project\Heart diases prediction\heart_diases_model.pkl")  # Make sure this file is in the same folder

# App title
st.title("❤️ Heart Disease Prediction App")
st.markdown("Enter patient details to predict risk of heart disease.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=45)
sex = st.selectbox("Sex", ["0 = Female", "1 = Male"])
cp = st.selectbox("Chest Pain Type (cp)", [
    "0 = Typical Angina", 
    "1 = Atypical Angina", 
    "2 = Non-anginal Pain", 
    "3 = Asymptomatic"
])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=50, max_value=250, value=120)
chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", ["0 = False", "1 = True"])
restecg = st.selectbox("Resting ECG (restecg)", [
    "0 = Normal", 
    "1 = ST-T Abnormality", 
    "2 = Left Ventricular Hypertrophy"
])
thalach = st.number_input("Max Heart Rate (thalach)", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise-Induced Angina (exang)", ["0 = No", "1 = Yes"])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope of ST Segment (slope)", [
    "0 = Upsloping", 
    "1 = Flat", 
    "2 = Downsloping"
])
ca = st.selectbox("Number of Major Vessels (ca)", ["0", "1", "2", "3", "4"])
thal = st.selectbox("Thalassemia (thal)", [
    "1 = Normal", 
    "2 = Fixed Defect", 
    "3 = Reversible Defect"
])

# Encode categorical values as integers
sex = int(sex[0])
cp = int(cp[0])
fbs = int(fbs[0])
restecg = int(restecg[0])
exang = int(exang[0])
slope = int(slope[0])
ca = int(ca)
thal = int(thal[0])

# Create feature array in correct order
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "🚨 High Risk of Heart Disease" if prediction == 1 else "✅ No Heart Disease Detected"
    
    st.subheader(f"Prediction: {result}")
