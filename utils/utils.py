import pandas as pd
import joblib

def load_data(path="data/synthetic_vehicle_sensor_data.csv"):
    return pd.read_csv(path, parse_dates=["timestamp"])

def load_model(path="models/random_forest_model.pkl"):
    return joblib.load(path)
