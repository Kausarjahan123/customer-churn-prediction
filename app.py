import streamlit as st
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import pandas as pd

# ---------------- LOAD MODEL SAFELY ---------------- #
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
features_path = os.path.join(os.path.dirname(__file__), "features.pkl")

model = pickle.load(open(model_path, "rb"))
features = pickle.load(open(features_path, "rb"))

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Customer Churn AI", layout="wide")

# ---------------- NETFLIX STYLE UI ---------------- #
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b0f19, #111827);
    color: white;
    font-family: Arial;
}

/* TITLE */
h1 {
    text-align: center;
    color: #ff1e1e !important;
    font-size: 54px;
    font-weight: 900;
}

/* SUB TEXT */
h2, h3, p, label {
    color: white !important;
    font-weight: 600;
}

/* INPUT BOXES */
div[data-baseweb="select"] > div {
    background-color: #1f2937 !important;
    color: white !important;
    border: 1px solid #ff1e1e !important;
}

/* INPUT FIELDS */
input {
    background-color: #1f2937 !important;
    color: white !important;
    border: 1px solid #ff1e1e !important;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(90deg, #ff1e1e, #b30000);
    color: white;
    border-radius: 10px;
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: 900;
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* RESULT BOX */
.stAlert {
    background-color: #111827 !important;
    border-left: 5px solid #ff1e1e !important;
    font-weight: bold;
}

/* PROGRESS BAR */
.stProgress > div > div {
    background-color: #ff1e1e !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.title("🎬 Customer Churn AI Dashboard")
st.markdown("<h3 style='text-align:center;'>AI-powered churn prediction system</h3>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- ENCODING ---------------- #
def encode(val):
    mapping = {
        "Yes": 1,
        "No": 0,
        "Female": 0,
        "Male": 1,
        "DSL": 0,
        "Fiber optic": 1,
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2,
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    }
    return mapping.get(val, val)

# ---------------- FEATURE IMPORTANCE ---------------- #
def show_feature_importance():
    importance = model.feature_importances_

    df_imp = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(by="Importance")

    fig, ax = plt.subplots()
    ax.barh(df_imp["Feature"], df_imp["Importance"], color="red")
    ax.set_title("Feature Importance")
    st.pyplot(fig)

# ---------------- INPUT UI ---------------- #
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure", 0, 100)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with col2:
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

MonthlyCharges = st.number_input("Monthly Charges", 0.0)
TotalCharges = st.number_input("Total Charges", 0.0)

st.markdown("---")

# ---------------- PREDICTION ---------------- #
if st.button("🚀 Predict Churn"):

    input_data = np.array([[
        encode(gender),
        SeniorCitizen,
        encode(Partner),
        encode(Dependents),
        tenure,
        encode(PhoneService),
        encode(MultipleLines),
        encode(InternetService),
        encode(OnlineSecurity),
        encode(OnlineBackup),
        encode(DeviceProtection),
        encode(TechSupport),
        encode(StreamingTV),
        encode(StreamingMovies),
        encode(Contract),
        encode(PaperlessBilling),
        encode(PaymentMethod),
        MonthlyCharges,
        TotalCharges
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("## 🎯 Result")

    if prediction == 1:
        st.error("⚠ Customer is likely to CHURN")
    else:
        st.success("✅ Customer will STAY")

    st.markdown("## 📊 Confidence Score")
    st.metric("Churn Probability", f"{probability*100:.2f}%")
    st.progress(float(probability))

    st.markdown("## 🧠 AI Explanation")

    if prediction == 1:
        st.write("Customer is likely to churn due to behavioral patterns such as contract type, tenure, and charges.")
    else:
        st.write("Customer shows stable long-term engagement and low churn risk.")

# ---------------- FEATURE IMPORTANCE TOGGLE ---------------- #
st.markdown("---")

if st.checkbox("📊 Show Feature Importance"):
    show_feature_importance()
