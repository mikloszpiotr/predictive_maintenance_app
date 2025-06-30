# Predictive Maintenance Dashboard

## 🏭 Business Problem
Industrial equipment generates continuous sensor data, but unexpected failures lead to costly downtime and maintenance. Predictive maintenance uses sensor analytics to anticipate failures and schedule maintenance proactively.

## 🎯 Business Impact
- **Reduced Downtime:** By predicting failures, maintenance teams can intervene before breakdowns.  
- **Cost Savings:** Targeted maintenance reduces unnecessary inspections and emergency repairs.  
- **Increased Safety:** Early alerts prevent hazardous equipment malfunctions.

## ⚙️ ML Solution
This app offers a simple predictive maintenance dashboard:
- **Data Preview:** Inspect timestamped sensor readings.  
- **Key Metrics:** Total records, time span, and failure count.  
- **Time-Series Charts:** Visualize each sensor’s readings over time.

## 📊 Data & Features
- **`data/predictive_data.csv`**: Default dataset with:
  - `timestamp` (datetime)
  - `sensor_1`, `sensor_2`, `sensor_3` (float readings)
  - `failure` (0/1 indicator)

- **`utils/utils.py`**:  
  - `load_data()`: Loads the default CSV, raises `FileNotFoundError` if missing.

## 🛠️ Setup & Installation

```bash
git clone <repo-url>
cd predictive_maintenance_app_complete
python -m venv .venv
# Activate virtual env (Windows):
.venv\Scripts\activate
# Or macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run app.py
```

- Upload your own CSV via the uploader, or rely on the default `data/predictive_data.csv`.

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
│   └── .gitkeep
└── utils/
    └── utils.py
```

## 🤝 Contributing
Enhancements welcome: add ML models, anomaly detection, or integrate real-time streams.
