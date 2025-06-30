# Predictive Maintenance Dashboard with Random Forest

## Business Problem
Prevent unplanned downtime by predicting equipment failures using sensor data.

## ML Solution
- **Model:** RandomForestClassifier (scikit-learn)
- **Features:** sensor_1, sensor_2, sensor_3
- **Evaluation:** classification_report on test split

## Usage
1. **Install**
   ```
   pip install -r requirements.txt
   streamlit run app.py
   ```
2. **Train Model:** Click "Train RandomForest Model" in the sidebar (uses default or uploaded data).
3. **Load Model:** Load an existing `models/rf_model.joblib`.
4. **View Predictions:** Scroll to see failure predictions & probabilities.

## Files
- `data/predictive_data.csv`: Sample dataset
- `utils/model.py`: Training, saving, loading & predicting
- `app.py`: Streamlit interface
