import streamlit as st
import pandas as pd
from utils.utils import load_data

def show_overview():
    st.title("Predictive Maintenance – Overview")

    # Allow users to upload their own CSV if the default isn't available
    uploaded_file = st.file_uploader(
        label="Upload a CSV file with sensor readings (timestamp, sensor_1, ..., failure)",
        type=['csv']
    )
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file, parse_dates=['timestamp'])
            st.success("Loaded uploaded CSV.")
        except Exception as e:
            st.error(f"Could not read uploaded file: {e}")
            return
    else:
        # Fallback to default data on disk
        try:
            data = load_data()
            st.info("Loaded default dataset from data/predictive_data.csv")
        except FileNotFoundError:
            st.error(
                "Default data file not found. "
                "Please upload a CSV above or ensure data/predictive_data.csv exists."
            )
            return

    # Display the data preview
    st.markdown("### Sensor Data Preview")
    st.dataframe(data.head())

    # Additional dashboard metrics could go here
