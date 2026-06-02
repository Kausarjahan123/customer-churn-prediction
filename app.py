import streamlit as st
import numpy as np
import pickle

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction System")
st.write("Enter customer details below:")

# ---------------- INPUTS ---------------- #
inputs = []

for feature in features:
    val = st.number_input(f"{feature}", value=0.0)
    inputs.append(val)

input_data = np.array([inputs])

# ---------------- PREDICTION ---------------- #
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write("### Result:")

    if prediction == 1:
        st.error("⚠ Customer will CHURN")
    else:
        st.success("✅ Customer will STAY")

    st.write("### Churn Probability:")
    st.info(f"{probability:.2f}")
