# Predictive Maintenance Dashboard

## 🏭 Business Problem
Industrial machinery and equipment generate continuous sensor data, but unplanned failures can cause costly downtime, safety hazards, and operational disruptions. Predictive maintenance leverages this sensor data to **anticipate equipment failures before they occur**, enabling proactive interventions that minimize unplanned outages.

## 🎯 Business Impact
- **Reduced Downtime:** Early failure detection cuts unexpected downtime by up to 50%, keeping production lines running smoothly.  
- **Cost Savings:** Prevents expensive emergency repairs and extends equipment life, saving maintenance costs by an estimated 20%.  
- **Improved Safety & Reliability:** Alerts maintenance teams to potential hazards, improving workplace safety and reducing the risk of catastrophic failures.

## ⚙️ ML Solution
We employ a **Random Forest Classifier** for its:
- **Robustness to Noisy Data:** Handles sensor noise and missing values well.  
- **Interpretability:** Feature importances help identify which sensors drive failure predictions.  
- **Fast Training & Scoring:** Suitable for interactive dashboards and quick retraining on new data.

### Model Details
- **Features:** `sensor_1`, `sensor_2`, `sensor_3` (continuous measurements)  
- **Target:** `failure` (binary indicator, 0 = no failure, 1 = failure)  
- **Hyperparameters:**  
  - `n_estimators=100` (balanced performance vs. training time)  
  - `random_state=42` (reproducibility)

## 🛠️ Application Features
1. **Data Ingestion:**  
   - Upload your own CSV or use the default `data/predictive_data.csv`.  
   - CSV must include: `timestamp`, `sensor_1`, `sensor_2`, `sensor_3`, `failure`.  
2. **Interactive Model Controls:**  
   - **Train Model:** Fit a new Random Forest on current data and view classification metrics.  
   - **Load Model:** Load previously trained model for immediate scoring.  
3. **Performance Metrics:**  
   - **Accuracy, Precision, Recall, F1 Score** displayed in dashboard.  
   - **Confusion Matrix** visualized with a heatmap.  
   - **Time-Series Chart:** Compare actual vs. predicted failures over time.  
4. **Visualization:**  
   - Data preview table.  
   - Line charts for individual sensor readings.  
   - Failure probability distribution per sample (in table).

## 🚀 Setup & Installation

```bash
git clone https://github.com/mikloszpiotr/predictive_maintenance_app.git
cd predictive_maintenance_app
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## ▶️ Running the App

```bash
streamlit run app.py
```

- Navigate to the sidebar to **train** or **load** the Random Forest model.  
- Scroll to view **performance metrics**, **confusion matrix**, and **actual vs. predicted** charts.

## 📁 Project Structure

```
predictive_maintenance_app/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── predictive_data.csv
├── models/
│   └── rf_model.joblib
└── utils/
    ├── utils.py
    └── model.py
```

## 🤝 Contributing
Contributions welcome! Suggestions include:
- Integrating additional sensors or feature engineering.  
- Experimenting with other models (e.g., Gradient Boosting, Neural Networks).  
- Adding alerting or scheduling for automated maintenance workflows.

## 📄 License
This project is licensed under the MIT License.
