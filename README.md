# Customer Churn Prediction System

## Project Overview

Customer churn prediction is a machine learning project designed to identify customers who are likely to discontinue a service.

Using customer account information and service usage patterns, the system predicts whether a customer will stay or leave, enabling businesses to take proactive retention actions.

---

## Business Problem

Customer retention is critical for subscription-based businesses.

Losing existing customers can significantly impact revenue and increase customer acquisition costs.

This project helps businesses identify at-risk customers early and implement targeted retention strategies.

---

## Problem Type

Machine Learning Classification Problem

Target Variable:

```text
Churn
```

* 1 = Customer likely to leave
* 0 = Customer likely to stay

---

## Dataset

Dataset Used:
Telco Customer Churn Dataset

Dataset Size:

* 7,000+ customer records

Features Include:

* Gender
* Senior Citizen Status
* Tenure
* Monthly Charges
* Total Charges
* Contract Type
* Internet Service
* Payment Method
* Partner Status
* Dependents

---

## Machine Learning Workflow

### Data Preprocessing

The following preprocessing steps were performed:

* Missing value handling
* Data cleaning
* Feature selection
* Categorical variable encoding
* Train-test split

### Feature Engineering

Customer attributes were transformed into machine-learning-ready features.

Important predictors included:

* Tenure
* Monthly Charges
* Contract Type
* Internet Service
* Payment Method

---

## Model Used

### Random Forest Classifier

Random Forest was selected because:

* Handles mixed feature types effectively
* Reduces overfitting through ensemble learning
* Provides strong classification performance
* Works well on structured tabular data

---

## Model Evaluation

Performance metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | XX%   |
| Precision | XX%   |
| Recall    | XX%   |
| F1 Score  | XX%   |

Replace the values above with your actual model results.

---

## Features

* Customer churn prediction
* Interactive Streamlit interface
* Real-time prediction generation
* Business-focused decision support
* User-friendly input form

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

---

## Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Screenshots

### Home Page

(Add screenshot)

### Prediction Form



### Prediction Output


---

## Skills Demonstrated

* Machine Learning
* Classification Modeling
* Feature Engineering
* Data Preprocessing
* Model Evaluation
* Streamlit Development
* Model Deployment
* Business Analytics

---

## Future Improvements

* Hyperparameter tuning
* Explainable AI using SHAP
* Cloud deployment
* Real-time prediction API
* MLOps pipeline implementation

---

## Author

Kausar Jahan

Aspiring Machine Learning Engineer
