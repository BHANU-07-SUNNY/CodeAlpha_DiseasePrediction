import streamlit as st
import joblib
import numpy as np

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}

.title{
    text-align:center;
    color:#d63384;
}

.result{
    font-size:25px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    background-color:#d63384;
    color:white;
    font-size:18px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("❤️ Heart Disease Prediction")

st.sidebar.info(
"""
This application predicts the possibility
of Heart Disease using Machine Learning.

Algorithms Used

✔ Logistic Regression

✔ Decision Tree

✔ Random Forest

✔ SVM
"""
)

st.sidebar.success("Developed using Streamlit")

# ---------------------------
# Title
# ---------------------------
st.markdown("<h1 class='title'>❤️ Heart Disease Prediction System</h1>", unsafe_allow_html=True)

st.write("Enter the patient's details below.")

st.divider()

# ---------------------------
# Input Fields
# ---------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Age",18,100)

    sex = st.selectbox("Gender",[0,1],format_func=lambda x:"Female" if x==0 else "Male")

    cp = st.selectbox(
        "Chest Pain Type",
        [0,1,2,3]
    )

    trestbps = st.number_input("Resting Blood Pressure",80,250)

    chol = st.number_input("Cholesterol",100,600)

    fbs = st.selectbox(
        "Fasting Blood Sugar >120",
        [0,1],
        format_func=lambda x:"No" if x==0 else "Yes"
    )

    restecg = st.selectbox(
        "Rest ECG",
        [0,1,2]
    )

with col2:

    thalach = st.number_input("Maximum Heart Rate",60,220)

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0,1],
        format_func=lambda x:"No" if x==0 else "Yes"
    )

    oldpeak = st.number_input("Old Peak",0.0,10.0)

    slope = st.selectbox(
        "Slope",
        [0,1,2]
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0,1,2,3]
    )

    thal = st.selectbox(
        "Thal",
        [0,1,2,3]
    )

# ---------------------------
# Prediction
# ---------------------------

if st.button("Predict Heart Disease"):

    features = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)

    confidence = np.max(probability)*100

    st.divider()

    if prediction==1:

        st.error("⚠ Heart Disease Detected")

    else:

        st.success("❤ No Heart Disease Detected")

    st.metric(
        label="Prediction Confidence",
        value=f"{confidence:.2f}%"
    )

st.divider()

st.caption("Heart Disease Prediction using Machine Learning | Streamlit")