import streamlit as st

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Overview", "Model Performance"])

if selection == "Overview":
    from pages.one_overview import show_overview
    show_overview()
else:
    from pages.two_model_performance import show_model_performance
    show_model_performance()
