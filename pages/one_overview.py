import streamlit as st
from utils.utils import load_data, load_model

def show_overview():
    st.title("Predictive Maintenance Dashboard – Overview")
    data = load_data()
    model = load_model()

    # Failure prediction timeline
    data["failure_prob"] = model.predict_proba(data[["sensor1", "sensor2", "sensor3"]])[:, 1]
    st.subheader("Failure Prediction Timeline")
    st.line_chart(data.set_index("timestamp")["failure_prob"])

    # KPI metrics
    st.subheader("Key Maintenance KPIs")
    total_hours = (data["timestamp"].iloc[-1] - data["timestamp"].iloc[0]).total_seconds() / 3600.0
    total_failures = int(data["failure"].sum())
    mtbf = total_hours / total_failures if total_failures > 0 else 0
    unplanned_downtime = total_failures * 5
    availability = ((total_hours - unplanned_downtime) / total_hours) * 100
    maintenance_cost_total = total_failures * 1000
    cost_per_unit = maintenance_cost_total / total_hours

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MTBF (hrs)", f"{mtbf:.1f}")
    col2.metric("Unplanned Downtime (hrs)", f"{unplanned_downtime}")
    col3.metric("Availability (%)", f"{availability:.1f}%")
    col4.metric("Cost per Unit", f"${cost_per_unit:.2f}")
