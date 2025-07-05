import streamlit as st
import pandas as pd
import Helper
from datetime import datetime

st.title('Covid-19 Analysis')
st.markdown("This app is created to analysis the Covid-19 data ")

data = Helper.load_data()
# Region selection
coun = st.selectbox('Select Country',['All Countries','Select Country'])

if coun =='All Countries':
    Countries = 'All Countries'
else:
    Countries = st.multiselect(
    'Select Country(s)',options=['Select Country'] + list(data['country'].unique()))
    Countries = [r for r in Countries if r != 'Select Country']
# Date selection
start_date = st.date_input('Start date', datetime(2020, 1, 1))
start_date = pd.to_datetime(start_date)
end_date = st.date_input('End date', datetime(2023, 1, 1))
end_date = pd.to_datetime(end_date)

# Disply Total Cases
st.header('Total Cases')
total_cases = Helper.countries_total_cases(Countries,start_date,end_date)
st.plotly_chart(total_cases)

# Disply Total Deaths
st.header('Total Deaths')
total_deaths = Helper.countries_total_deaths(Countries,start_date,end_date)
st.plotly_chart(total_deaths)
