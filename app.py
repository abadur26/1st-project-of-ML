import streamlit as st
import pickle
import pandas as pd
import sklearn

# Load files
model = pickle.load(open("stress_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
target_encoder = pickle.load(open("target_encoder.pkl", "rb"))

st.title("Stress Level Prediction App")

# Example user input
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
smoking = st.selectbox("Smoking", ["Yes", "No", "Unknown"])
alcohol = st.selectbox("Alcohol Consumption", ["Moderate", "Heavy", "Unknown"])
age = st.number_input("Age", min_value=1, max_value=120, step=1)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, step=1)

# Encode inputs
input_data = pd.DataFrame({
    "Gender": [label_encoders["Gender"].transform([gender])[0]],
    "Smoking": [label_encoders["Smoking"].transform([smoking])[0]],
    "Alcohol_Consumption": [label_encoders["Alcohol_Consumption"].transform([alcohol])[0]],
    "Age": [age],
    "BMI": [bmi],
    "Heart_Rate": [heart_rate]
})

# Scale
input_scaled = scaler.transform(input_data)

# Predict
prediction = model.predict(input_scaled)[0]
predicted_class = target_encoder.inverse_transform([int(round(prediction))])[0]
st.button("Submit")

st.subheader(f"Predicted Stress Level: {predicted_class}")
