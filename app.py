import streamlit as st
import numpy as np
import pickle

# Load model and features
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

st.title("📊 Customer Churn Prediction System")
st.write("Enter customer details below")

inputs = []

for feature in features:
    value = st.number_input(
        f"{feature}",
        value=0.0
    )
    inputs.append(value)

input_data = np.array([inputs])

if st.button("Predict Churn"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")

    st.subheader("Churn Probability")
    st.info(f"{probability:.2%}")
