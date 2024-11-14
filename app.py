import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
model_path = 'LinearRegressionModel.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# UI for the Streamlit app
st.title("Car Price Prediction")

# Dropdown for selecting car attributes
company = st.selectbox("Select Company", ["Maruti", "Hyundai", "Tata", "Toyota", "Honda"])
car_model = st.selectbox("Select Model", ["Swift", "i20", "Nexon", "Innova", "City"])
year = st.selectbox("Select Year of Purchase", [2018, 2019, 2020, 2021, 2022])
fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])

# Input for kilometers traveled
kms_driven = st.number_input("Enter the number of kilometers the car has traveled", min_value=0)

# Button to predict price
if st.button("Predict Price"):
    # Prepare input data
    input_data = pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    try:
        # Predict price
        predicted_price = model.predict(input_data)[0]
        # Display the predicted price
        st.write(f"The estimated price of the car is: ₹ {predicted_price:,.2f}")
    except Exception as e:
        # Handle errors in prediction
        st.error(f"An error occurred during prediction: {e}")
