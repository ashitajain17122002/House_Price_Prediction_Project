import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open("House Price Prediction.pkl", "rb"))
# import joblib
# model = joblib.load("House Price Prediction.pkl")

data = pd.read_csv("Cleaned_data.xls")

st.header("Bangalore House Price Prediction")
loc = st.selectbox("Choose The Location", data["location"].unique())
sqft = st.number_input("Enter Total Sqft")
bed = st.number_input("Enter No. of Bedrooms")
bathroom = st.number_input("Enter No. of Bathrooms")
balcony = st.number_input("Enter No. of Balconies")

input = pd.DataFrame([[loc, sqft, bed, bathroom, balcony]], columns = ["location", "total_sqft", "bedrooms", "bath","balcony"])

if st.button("Predict Price"):
    output = model.predict(input)
    output_str = "Price of the House is: " + str(round(output[0]*1000000, 2))
    st.write(output_str)