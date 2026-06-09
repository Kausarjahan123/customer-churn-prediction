import streamlit as st
import numpy as np
import pickle

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Churn AI", layout="wide")

# ---------------- NETFLIX STYLE UI ---------------- #
st.markdown("""
<style>
.stApp {
    background-color: #0b0f19;
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #E50914;
    font-size: 50px;
    font-weight: 900;
}

/* Buttons */
.stButton > button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    width: 100%;
    height: 45px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #b00610;
}

/* Inputs */
.stSelectbox, .stNumberInput {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.title("🎬 Customer Churn AI (Netflix Style)")

st.write("Predict whether a customer will stay or leave using AI 🚀")

st.markdown("---")

# ---------------- ENCODING FUNCTION ---------------- #
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

# ---------------- UI INPUTS ---------------- #
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", 0, 100)
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

    st.markdown("## 📊 Churn Probability")
    st.info(f"{probability * 100:.2f}%")

    st.progress(float(probability))
