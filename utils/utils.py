import os
import pandas as pd

# Construct path relative to this utils file
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'predictive_data.csv')

def load_data():
    """Load the predictive maintenance dataset."""
    # Ensure the path is normalized
    path = os.path.normpath(DATA_PATH)
    return pd.read_csv(path, parse_dates=['timestamp'])
