st.markdown("""
<style>

/* ===== GLOBAL BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #0b0f19, #111827);
    color: #ffffff;
    font-family: 'Arial';
}

/* ===== TITLE ===== */
h1 {
    text-align: center;
    color: #ff1e1e !important;
    font-size: 54px;
    font-weight: 900;
    text-shadow: 2px 2px 10px rgba(255,0,0,0.4);
}

/* ===== SUBTEXT ===== */
p, label {
    color: #ffffff !important;
    font-weight: 600;
}

/* ===== INPUT BOXES ===== */
div[data-baseweb="select"] > div {
    background-color: #1f2937 !important;
    color: white !important;
    border: 1px solid #ff1e1e !important;
}

input {
    background-color: #1f2937 !important;
    color: white !important;
    border: 1px solid #ff1e1e !important;
}

/* ===== BUTTON ===== */
.stButton > button {
    background: linear-gradient(90deg, #ff1e1e, #b30000);
    color: white;
    border-radius: 10px;
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: 900;
    border: none;
    box-shadow: 0px 4px 15px rgba(255, 0, 0, 0.4);
}

.stButton > button:hover {
    background: #ff0000;
    transform: scale(1.02);
}

/* ===== RESULT BOX ===== */
.stAlert {
    background-color: #111827 !important;
    color: white !important;
    border-left: 5px solid #ff1e1e !important;
    font-weight: bold;
}

/* ===== PROGRESS BAR ===== */
.stProgress > div > div {
    background-color: #ff1e1e !important;
}

</style>
""", unsafe_allow_html=True)
