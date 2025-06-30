import streamlit as st
import pandas as pd
from utils.utils import load_data

def show_overview():
    st.title("Predictive Maintenance – Overview")
    uploaded = st.file_uploader("Upload CSV (timestamp,sensor_1,...,failure)", type=['csv'])
    if uploaded is not None:
        try:
            data = pd.read_csv(uploaded, parse_dates=['timestamp'])
            st.success("Loaded uploaded data")
        except Exception as e:
            st.error(f"Error reading uploaded file: {e}")
            return
    else:
        try:
            data = load_data()
            st.info("Loaded default predictive_data.csv")
        except FileNotFoundError:
            st.error("Default data not found. Please upload a CSV above.")
            return

    st.markdown("### Sensor Data Preview")
    st.dataframe(data.head())
