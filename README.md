# Todoist Analytics

## Setup
1. Create a virtual environment (example on Unix-like systems):
   ```
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies from requirements.txt:
   ```
   pip install -r requirements.txt
   ```

## Data
Place your CSV files into the `data` folder.

## Running the App
Use Streamlit to run the app:
```
streamlit run app.py
```
If you need to keep the app running after closing the terminal (on Unix-like systems), you can try:
```
nohup streamlit run app.py &
```