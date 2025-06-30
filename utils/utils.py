import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'predictive_data.csv')

def load_data():
    path = os.path.normpath(DATA_PATH)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found at {path}")
    return pd.read_csv(path, parse_dates=['timestamp'])
