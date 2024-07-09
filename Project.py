import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression
import streamlit as st
import pickle


model = pickle.load(open(r"linear_reg.plk",'rb'))

st.title("House Price Prediction")
         
SquareFeet = st.number_input("Enter the size of the house",min_value = 600, max_value = 5000, step = 50)
Bedrooms = st.number_input("Enter the number of bedrooms",min_value = 0, max_value = 5, step = 1)	
Bathrooms = st.number_input("Enter the number of bathrooms",min_value = 0, max_value = 5, step = 1)	
Neighborhood = st.radio("Enter the neighbourhood",['Rural','Urban','Suburb'])
neighbor = 1 if Neighborhood=="Rural" else 2 if Neighborhood=="Urban" else 3

YearBuilt = st.number_input("Enter the number of year of construction",min_value = 1900, max_value = 2030, step = 1)

price = model.predict([[SquareFeet,Bedrooms,Bathrooms,neighbor,YearBuilt]])

if st.button('Submit'):
    st.write("The price for the flat with given details is Rs.",price)
    
    







