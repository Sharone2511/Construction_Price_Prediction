import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('construction_price.sav', 'rb'))

st.title("Construction Price Prediction")

st.subheader("Enter the feature values below:")

# User inputs for all features
building_permits = st.number_input("Building Permits", value=2000)
const_price_index = st.number_input("Construction Price Index", value=1800)
delinquency_rate = st.number_input("Delinquency Rate", value=145.0)
GDP = st.number_input("GDP", value=1.97)
house_for_sale_or_sold = st.number_input("Houses for Sale or Sold", value=15000)
housing_subsidies = st.number_input("Housing Subsidies", value=80)
income = st.number_input("Income", value=25.0)
interest_rate = st.number_input("Interest Rate", value=10700.0)
mortgage_rate = st.number_input("Mortgage Rate", value=1.2)
construction_unit = st.number_input("Construction Unit", value=5.9)
total_houses = st.number_input("Total Houses", value=1650)
total_const_spending = st.number_input("Total Construction Spending", value=110000.0)
unemployment_rate = st.number_input("Unemployment Rate", value=1.5)
urban_population = st.number_input("Urban Population", value=80.0)

# Button to predict
if st.button("Predict Home Price Index"):
    # Prepare input array
    input_data = np.array([[building_permits,
                            const_price_index,
                            delinquency_rate,
                            GDP,
                            house_for_sale_or_sold,
                            housing_subsidies,
                            income,
                            interest_rate,
                            mortgage_rate,
                            construction_unit,
                            total_houses,
                            total_const_spending,
                            unemployment_rate,
                            urban_population]])
    
    # Predict
    predicted_price = model.predict(input_data)[0]
    
    # Display result
    st.success(f"Predicted Price: {predicted_price:.2f}")
