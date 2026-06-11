import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.hero {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 2rem;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}

.metric-card {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #667eea;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>🎓 Student Performance Predictor</h1>
    <p>AI-powered grade prediction using machine learning</p>
</div>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Student Information")

    studytime = st.slider(
        "Study Time",
        min_value=1,
        max_value=4,
        value=2
    )

    failures = st.slider(
        "Previous Failures",
        min_value=0,
        max_value=5,
        value=0
    )

    absences = st.slider(
        "Absences",
        min_value=0,
        max_value=50,
        value=5
    )

    predict_btn = st.button(
        "🚀 Predict Performance",
        use_container_width=True
    )

with col2:
    st.subheader("📈 Live Summary")

    st.metric("Study Time", studytime)
    st.metric("Failures", failures)
    st.metric("Absences", absences)

if predict_btn:
    data = pd.DataFrame(
        [[studytime, failures, absences]],
        columns=["studytime", "failures", "absences"]
    )

    prediction = model.predict(data)[0]

    st.success("Prediction Complete!")

    score = max(0, min(20, prediction))

    st.metric(
        label="Predicted Final Grade",
        value=f"{score:.1f}/20"
    )

    progress = int((score / 20) * 100)
    st.progress(progress)

    if score >= 15:
        st.balloons()
        st.success("🌟 Excellent performance expected!")
    elif score >= 10:
        st.info("👍 Good performance expected!")
    else:
        st.warning("📚 Additional study may be beneficial.")
