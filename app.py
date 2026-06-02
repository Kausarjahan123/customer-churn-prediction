import streamlit as st
import numpy as np
import pickle

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction System")
st.write("Enter customer details to predict whether they will leave or stay")

# ---------------- INPUT FIELDS ---------------- #
age = st.number_input("Age", 18, 100)
tenure = st.number_input("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0, 500)
total_charges = st.number_input("Total Charges", 0, 10000)

# You can extend these later
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# ---------------- ENCODING SIMPLE INPUT ---------------- #
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}

input_data = np.array([[
    age,
    tenure,
    monthly_charges,
    total_charges,
    contract_map[contract],
    internet_map[internet]
]])

# ---------------- PREDICTION ---------------- #
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ Customer is likely to CHURN")
    else:
        st.success("✅ Customer will STAY")
