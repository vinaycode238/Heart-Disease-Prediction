# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

This project is a Machine Learning based Heart Disease Prediction system that predicts whether a person is likely to have heart disease based on medical information.

The project uses a Random Forest Classifier along with a preprocessing pipeline for data preprocessing and prediction.

A Streamlit web application is also created where users can upload a CSV file and get predictions with disease probabilities.

---

## 🎯 Objective

The main objective of this project is to build an end-to-end machine learning application that can:

- Preprocess healthcare data
- Train a machine learning model
- Predict heart disease
- Calculate prediction probability
- Accept CSV files as input
- Display prediction results
- Allow users to download predictions as a CSV file
- Provide a simple web interface using Streamlit

---

## 🧠 Machine Learning Model

### Random Forest Classifier

The project uses a Random Forest Classifier with:

- Number of estimators: 200
- Random state: 42

The model achieved approximately:

**Accuracy: 86.84%**

> Note: This project is for educational and demonstration purposes and should not be used as a medical diagnostic tool.

---

## 📊 Features Used

The model uses the following features:

### Numerical Features

- Age
- Resting Blood Pressure
- Cholesterol
- Maximum Heart Rate
- Oldpeak

### Categorical Features

- Sex
- Chest Pain Type
- Fasting Blood Sugar
- Resting ECG
- Exercise Induced Angina
- Slope
- CA
- Thal

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🔄 Project Workflow

```text
Data Collection
       ↓
Data Cleaning & EDA
       ↓
Feature Selection
       ↓
Train-Test Split
       ↓
Data Preprocessing
       ↓
Random Forest Model
       ↓
Model Evaluation
       ↓
Model Saving
       ↓
Streamlit Web Application
       ↓
CSV Upload
       ↓
Prediction
       ↓
Prediction Probability
       ↓
Download Results