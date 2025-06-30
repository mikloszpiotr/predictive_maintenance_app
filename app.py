import streamlit as st
import pandas as pd
import os
from utils.utils import load_data

st.set_page_config(page_title='Predictive Maintenance Dashboard', layout='wide')

st.title("Predictive Maintenance Dashboard – Overview")

# Data upload or default
uploaded = st.file_uploader(
    "Upload sensor data CSV (timestamp,sensor_1,...,failure)",
    type=['csv']
)
if uploaded is not None:
    try:
        data = pd.read_csv(uploaded, parse_dates=['timestamp'])
        st.success("Loaded uploaded data")
    except Exception as e:
        st.error(f"Error reading uploaded file: {e}")
        st.stop()
else:
    try:
        data = load_data()
        st.info("Loaded default data from data/predictive_data.csv")
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

# Preview and metrics
st.subheader("Sensor Data Preview")
st.dataframe(data.head(), use_container_width=True)

st.subheader("Basic Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(data))
col2.metric("Time Range", f"{data['timestamp'].min()} to {data['timestamp'].max()}")
col3.metric("Failure Count", int(data['failure'].sum()))

# Time series charts
st.subheader("Sensor Readings Over Time")
for sensor in [c for c in data.columns if c.startswith('sensor_')]:
    st.line_chart(data.set_index('timestamp')[sensor])
