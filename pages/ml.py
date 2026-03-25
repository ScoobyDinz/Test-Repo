# TESTING FILE FOR STREAMLIT NAVIGATION SIDE-PANEL

import streamlit as st

st.write("TESTING FROM THE FORECASTS PAGE")

import joblib
import pandas as pd

# Load model + features
model = joblib.load("solar_model.pkl")
features = joblib.load("features.pkl")

def predict_solar(year, month, last_month_share):
    input_data = pd.DataFrame([{
        "year": year,
        "month": month,
        "solar_share_lag1": last_month_share
    }])

    prediction = model.predict(input_data)[0]
    return prediction
