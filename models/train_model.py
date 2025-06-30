import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the synthetic data
data = pd.read_csv("data/synthetic_vehicle_sensor_data.csv")
X = data[["sensor1", "sensor2", "sensor3"]]
y = data["failure"]

# Train-test split (time-based)
train_size = int(0.7 * len(data))
X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate on test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2%}")

# Save the trained model to disk
os.makedirs(os.path.dirname("models/random_forest_model.pkl"), exist_ok=True)
joblib.dump(model, "models/random_forest_model.pkl")
