import streamlit as st
import pandas as pd
# Title
st.title("Stress Level Prediction App")
# User input fields
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
smoking = st.selectbox("Smoking", ["Yes", "No"])
alcohol = st.selectbox("Alcohol Consumption", ["Moderate", "Heavy", "NaN"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=150, value=80)

# Convert categorical inputs to numeric (simple mapping)
gender_map = {"Male": 1, "Female": 0, "Other": 2}
smoking_map = {"Yes": 1, "No": 0}
alcohol_map = {"Moderate": 1, "Heavy": 2, "NaN": 0}

# Prepare input data
input_data = pd.DataFrame({
    "Gender": [gender_map[gender]],
    "Smoking": [smoking_map[smoking]],
    "Alcohol_Consumption": [alcohol_map[alcohol]],
    "Age": [age], "BMI": [bmi], "Heart_Rate": [heart_rate] })

 # Predict
if st.button("Predict Stress Level"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Stress Level: {prediction}")

