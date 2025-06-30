# Predictive Vehicle Maintenance App

## Problem Statement
Unplanned equipment failures in transportation assets lead to significant downtime, safety risks, and high maintenance costs. Predicting part failures before they occur allows maintenance teams to intervene proactively, ensuring vehicles stay operational and reducing overall lifecycle expenses.

## Why This Problem Matters
- **Cost Savings:** Reactive repairs are often more expensive than planned maintenance.  
- **Operational Efficiency:** Unexpected breakdowns disrupt schedules, leading to lost productivity.  
- **Safety:** Preventing failures reduces the risk of accidents caused by faulty components.  
- **Asset Longevity:** Timely maintenance extends the working life of expensive vehicle parts.

## Why Random Forest?
- **Robust Performance:** Ensemble of decision trees reduces overfitting and handles noisy sensor data well.  
- **Interpretability:** Feature importance scores help identify which sensors most influence failure predictions.  
- **Fast Training & Inference:** Suitable for real-time or near-real-time analytics in production.  
- **Proven in Maintenance:** Widely used in industry for classification tasks and anomaly detection in condition monitoring.

## How Random Forest Works
A Random Forest builds multiple decision trees on random subsets of data and features. Each tree votes on whether a failure is imminent. The final prediction is the majority vote across all trees, which:
1. **Reduces variance** compared to a single decision tree.  
2. **Improves generalization** across different failure scenarios.  
3. **Aggregates diverse insights** from multiple tree structures to yield a robust classifier.

## Our Solution Approach
1. **Synthetic Data Generation:** We simulate time-series sensor readings (e.g., temperature, vibration) that rise until a failure threshold triggers.  
2. **Model Training:** The Random Forest classifier is trained on historical sensor data with binary failure labels.  
3. **Interactive Dashboard:** A Streamlit app visualizes:
   - **Failure Prediction Timeline:** Model-predicted risk probability over time.  
   - **Maintenance KPIs:** MTBF, unplanned downtime, availability, and cost per unit.  
   - **Model Performance:** Accuracy, confusion matrix, and ROC curve.  
4. **Modular Design:** Separate folders for data simulation, model training, utilities, and Streamlit pages ensure clean code organization.

By combining robust machine learning with an intuitive dashboard, this app enables maintenance teams to anticipate failures, optimize schedules, and improve fleet reliability.
