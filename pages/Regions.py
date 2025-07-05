import streamlit as st
import pandas as pd
import Helper
from datetime import datetime

st.title('Covid-19 Analysis')
st.markdown("This app is created to analysis the Covid-19 data ")

data = Helper.load_data()
# Region selection
reg = st.selectbox('Select Region',['All Regions','Select Region'])

if reg =='All Regions':
    regions = 'All Regions'
else:
    regions = st.multiselect(
    'Select Region(s)',options=['Select Region'] + list(data['who_region'].unique()))
    regions = [r for r in regions if r != 'Select Region']
# Date selection
start_date = st.date_input('Start date', datetime(2020, 1, 1))
start_date = pd.to_datetime(start_date)
end_date = st.date_input('End date', datetime(2023, 1, 1))
end_date = pd.to_datetime(end_date)

# Disply Total Cases
st.header('Total Cases')
total_cases = Helper.regions_total_cases(regions,start_date,end_date)
st.plotly_chart(total_cases)

# Disply Total Deaths
st.header('Total Deaths')
total_deaths = Helper.regions_total_deaths(regions,start_date,end_date)
st.plotly_chart(total_deaths)
