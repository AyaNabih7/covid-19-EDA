import streamlit as st
import pandas as pd 


st.title('Covid-19 Dataset')
st.markdown(" ")
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("**Dataset Overview**  \nThis dataset contains global Covid-19 statistics including confirmed cases, deaths, recoveries,"
        " and vaccination rates. It is sourced from reliable health organizations and updated regularly for accurate analysis.")
    with col2:
        st.image('https://themwl.org/sites/default/files/who-logo_0.jpg',
                width = 250)

@st.cache_data
def load_data():
    df = pd.read_csv('COVID-19.csv')
    df['Date_reported']= pd.to_datetime(df['Date_reported'])
    df.columns = df.columns.str.lower()
    return df
df =load_data()

st.header('Data')
if st.checkbox('Show Data'):
    st.write(df)

st.header('Description')
st.markdown("""
This dataset includes time-series and regional data related to the Covid-19 pandemic.  
It can be used to perform statistical analysis, visualize global trends, and study the progression of the virus over time.  
Typical columns may include:
- Country/Region  
- Date  
- Confirmed Cases  
- Deaths  
- Recoveries  
- Vaccinations  

The data is essential for researchers, analysts, and decision-makers to understand the impact and spread of the virus.
""")
