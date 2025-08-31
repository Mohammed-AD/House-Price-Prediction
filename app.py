import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open(r"C:\Users\Lenovo\Desktop\House pridiction Project\House_prediction_mode.pkl",'rb'))

st.header('Banglore House Prices Predictor')

data =pd.read_csv(r'C:\Users\Lenovo\Desktop\House pridiction Project\Cleaned_data.csv')

loc= st.selectbox('Choose the location', data['location'].unique())
sqft= st.number_input('Enter Total Sqft')
beds= st.number_input('Enter No of Bedrooms')
bath= st.number_input('Enter No of Bathrooms')
balc= st.number_input('Enter No of Balconies')

input =pd.DataFrame([[loc,sqft,bath,balc,beds]], columns= ['location','total_sqft','bath','balcony','bedrooms'])

if st.button("Predict Price"):
    output= model.predict(input)
    out_str = 'Price of the House is '+ str(round(output[0]*100000,2))
    st.success(out_str)