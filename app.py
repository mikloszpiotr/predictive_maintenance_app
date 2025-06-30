import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

from utils.utils import load_data
from utils.model import train_model, predict, load_model, MODEL_PATH

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

st.set_page_config(page_title='Predictive Maintenance Dashboard', layout='wide')
st.title("Predictive Maintenance Dashboard")

# Upload or load data
uploaded = st.file_uploader("Upload sensor CSV", type=['csv'])
if uploaded:
    data = pd.read_csv(uploaded, parse_dates=['timestamp'])
    st.success("Loaded uploaded data")
else:
    try:
        data = load_data()
        st.info("Loaded default data from data/predictive_data.csv")
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

# Data preview
st.subheader("Data Preview")
st.dataframe(data.head(), use_container_width=True)

# Sidebar: Train or load model
st.sidebar.header("Model Controls")
if st.sidebar.button("Train RandomForest Model"):
    clf, report = train_model(data)
    st.sidebar.success("Model trained and saved")
    st.sidebar.subheader("Evaluation Report")
    st.sidebar.json(report)
elif st.sidebar.button("Load Model"):
    try:
        clf = load_model()
        st.sidebar.success("Model loaded")
    except FileNotFoundError as e:
        st.sidebar.error(str(e))
        st.stop()

# Predictions and performance
if os.path.exists(os.path.join('models', 'rf_model.joblib')):
    st.subheader("Predictions")
    results = predict(data)
    st.dataframe(results[['timestamp','sensor_1','sensor_2','sensor_3','predicted_failure','failure_prob']].head(), use_container_width=True)

    # Compute metrics
    y_true = results['failure']
    y_pred = results['predicted_failure']
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    st.subheader("Model Performance")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Accuracy", f"{acc:.2f}")
    m2.metric("Precision", f"{prec:.2f}")
    m3.metric("Recall", f"{rec:.2f}")
    m4.metric("F1 Score", f"{f1:.2f}")

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    st.subheader("Confusion Matrix")
    fig, ax = plt.subplots()
    cax = ax.matshow(cm)
    for (i, j), val in np.ndenumerate(cm):
        ax.text(j, i, str(val), ha='center', va='center')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    st.pyplot(fig)

    # Actual vs Predicted over time
    st.subheader("Actual vs Predicted Failures Over Time")
    time_df = results.set_index('timestamp')[['failure', 'predicted_failure']]
    st.line_chart(time_df)
