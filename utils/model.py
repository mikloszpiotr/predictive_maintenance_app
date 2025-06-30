import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'rf_model.joblib')

def train_model(df, test_size=0.2, random_state=42):
    X = df[['sensor_1', 'sensor_2', 'sensor_3']]
    y = df['failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    clf = RandomForestClassifier(n_estimators=100, random_state=random_state)
    clf.fit(X_train, y_train)
    # Evaluation report
    report = classification_report(y_test, clf.predict(X_test), output_dict=True)
    # Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    return clf, report

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Train first.")
    return joblib.load(MODEL_PATH)

def predict(df):
    clf = load_model()
    X = df[['sensor_1', 'sensor_2', 'sensor_3']]
    preds = clf.predict(X)
    probs = clf.predict_proba(X)[:,1]
    result = df.copy()
    result['predicted_failure'] = preds
    result['failure_prob'] = probs
    return result
