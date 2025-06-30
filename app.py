import streamlit as st
import pandas as pd
import os
from utils.utils import load_data
from utils.model import train_model, predict, load_model, MODEL_PATH

st.set_page_config(page_title='Predictive Maintenance Dashboard', layout='wide')
st.title("Predictive Maintenance Dashboard")

# Load data
uploaded = st.file_uploader("Upload sensor CSV", type=['csv'])
if uploaded:
    data = pd.read_csv(uploaded, parse_dates=['timestamp'])
    st.success("Loaded uploaded data")
else:
    try:
        data = load_data()
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

# Data preview
st.subheader("Data Preview")
st.dataframe(data.head(), use_container_width=True)

# Sidebar: train or load model
st.sidebar.header("Model")
if st.sidebar.button("Train RandomForest Model"):
    clf, report = train_model(data)
    st.sidebar.success("Model trained and saved")
    st.sidebar.json(report)
elif st.sidebar.button("Load Model"):
    try:
        clf = load_model()
        st.sidebar.success("Model loaded")
    except FileNotFoundError as e:
        st.sidebar.error(str(e))
        st.stop()

# If model exists, show predictions
if os.path.exists(os.path.join('models','rf_model.joblib')):
    st.subheader("Predictions")
    results = predict(data)
    st.dataframe(results[['timestamp','sensor_1','sensor_2','sensor_3','predicted_failure','failure_prob']].head(), use_container_width=True)
