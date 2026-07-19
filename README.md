"# CodeAlpha_DiseasePrediction" 
# ❤️ Heart Disease Prediction using Machine Learning

A Machine Learning-based web application that predicts the likelihood of heart disease using patient medical data. This project was developed as part of the **CodeAlpha Machine Learning Internship** and includes data preprocessing, model training, evaluation, and a user-friendly Streamlit interface.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help patients seek timely medical attention and improve treatment outcomes.

This project uses the **UCI Heart Disease Dataset** to train multiple machine learning models and predict whether a patient is likely to have heart disease based on clinical parameters.

---

## 🎯 Objectives

- Predict the presence of heart disease using machine learning.
- Compare the performance of multiple classification algorithms.
- Build an interactive web application using Streamlit.
- Provide an easy-to-use interface for making predictions.

---

## 📂 Dataset

- **Dataset:** UCI Heart Disease Dataset
- **Source:** UCI Machine Learning Repository
- **Number of Records:** 303
- **Number of Features:** 13
- **Target Variable:** Presence of Heart Disease

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Algorithms

The following classification algorithms were implemented and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

The best-performing model was saved and used for prediction in the Streamlit application.

---

## 📊 Features Used

The prediction is based on the following medical parameters:

- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate Achieved
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- Slope of Peak Exercise ST Segment
- Number of Major Vessels (CA)
- Thalassemia

---



## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/CodeAlpha_DiseasePrediction.git
```

### Navigate to the project directory

```bash
cd CodeAlpha_DiseasePrediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 How It Works

1. Load the trained machine learning model.
2. Enter the patient's medical information.
3. Click the **Predict Heart Disease** button.
4. The application processes the input and predicts whether heart disease is likely.
5. The prediction result is displayed along with the confidence score.

---

## 📈 Model Workflow

- Data Collection
- Data Preprocessing
- Handling Missing Values
- Feature Selection
- Data Scaling
- Train-Test Split
- Model Training
- Model Evaluation
- Model Saving
- Streamlit Deployment

---

## 📋 Requirements

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

---

## 🎓 Internship Information

**Internship:** CodeAlpha Machine Learning Internship

**Task:** Disease Prediction from Medical Data

---

## 🔮 Future Improvements

- Support prediction for multiple diseases.
- Add advanced visualization dashboards.
- Integrate additional machine learning models.
- Deploy the application on Streamlit Community Cloud.
- Improve model performance through hyperparameter tuning.

---

## 👨‍💻 Author

**Bhanu Prakash**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Data Science)

SASTRA Deemed University

GitHub: https://github.com/BHANU-07-SUNNY

---

## ⭐ Acknowledgements

- UCI Machine Learning Repository
- Scikit-learn Documentation
- Streamlit Documentation
- CodeAlpha
