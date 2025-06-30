# Predictive Vehicle Maintenance App

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Generate synthetic data:
   ```
   python data/simulate_data.py
   ```

3. Train the model:
   ```
   python models/train_model.py
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Project Structure

- `data/`: synthetic data generator and dataset  
- `models/`: model training script and saved model  
- `utils/`: utility functions for loading data and model  
- `pages/`: Streamlit pages for the dashboard  
- `app.py`: main app with navigation  
- `requirements.txt`: Python dependencies  
- `README.md`: project instructions  
