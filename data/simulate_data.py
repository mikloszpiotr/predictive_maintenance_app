import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# Simulation parameters
num_hours = 1000
sensor1_threshold = 80.0

# Initialize lists for data
timestamps = []
sensor1_vals = []
sensor2_vals = []
sensor3_vals = []
failure_flags = []

# Starting values
sensor1 = 20.0  # initial healthy value for Sensor1
for hour in range(num_hours):
    timestamps.append(pd.Timestamp("2025-01-01") + pd.Timedelta(hours=hour))
    sensor1_vals.append(sensor1)
    sensor2_vals.append(30.0 + np.random.normal(0, 5))
    sensor3_vals.append(50.0 + np.random.normal(0, 5))
    if sensor1 >= sensor1_threshold:
        failure_flags.append(1)
        sensor1 = 20.0
    else:
        failure_flags.append(0)
    sensor1 += np.random.uniform(0.2, 1.0)

# Create the DataFrame
data = pd.DataFrame({
    "timestamp": timestamps,
    "sensor1": sensor1_vals,
    "sensor2": sensor2_vals,
    "sensor3": sensor3_vals,
    "failure": failure_flags
})

# Save to CSV
os.makedirs(os.path.dirname("data/synthetic_vehicle_sensor_data.csv"), exist_ok=True)
data.to_csv("data/synthetic_vehicle_sensor_data.csv", index=False)
