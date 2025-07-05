import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('COVID-19.csv')
    df['Date_reported']= pd.to_datetime(df['Date_reported'])
    df.columns = df.columns.str.lower()
    return df
df =load_data()

def regions_total_cases(regions,start_date=df.date_reported.min(),end_date=df.date_reported.max()):
    if regions !='All Regions':
        if isinstance(regions, str):
            regions = [regions]
        temp_df = df[df['who_region'].isin(regions)]
    else:
        temp_df = df
    fig = px.histogram(temp_df,x ='date_reported',y='new_cases',title='Total Cases',range_x=[start_date,end_date],nbins=50)
    return fig

def regions_total_deaths(regions,start_date=df.date_reported.min(),end_date=df.date_reported.max()):
    if regions !='All Regions':
        if isinstance(regions, str):
            regions = [regions] 
        temp_df = df[df['who_region'].isin(regions)]
    else:
        temp_df = df
    fig = px.histogram(temp_df,x ='date_reported',y='new_deaths',title='Total Cases',range_x=[start_date,end_date],nbins=50)
    return fig

def countries_total_cases(countries,start_date=df.date_reported.min(),end_date=df.date_reported.max()):
    if countries !='All Countries':
        if isinstance(countries, str):
            countries = [countries] 
        temp_df = df[df['country'].isin(countries)]
    else:
        temp_df = df
    fig = px.histogram(temp_df,x ='date_reported',y='new_cases',title='Total Cases',range_x=[start_date,end_date],nbins=50)
    return fig

def countries_total_deaths(countries,start_date=df.date_reported.min(),end_date=df.date_reported.max()):
    if countries !='All Countries':
        if isinstance(countries, str):
            countries = [countries] 
        temp_df = df[df['country'].isin(countries)]
    else:
        temp_df = df
    fig = px.histogram(temp_df,x ='date_reported',y='new_deaths',title='Total Cases',range_x=[start_date,end_date],nbins=50)
    return fig