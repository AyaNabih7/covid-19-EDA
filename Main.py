import streamlit as st

st.title('Covid-19 Analysis')
st.markdown("This app is created to analysis the Covid-19 data ")
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("""
**WHO Covid-19 Official Dashboard**  
The official dashboard provided by the World Health Organization (WHO) offers up-to-date global statistics on confirmed cases, deaths, and vaccination progress. It serves as a reliable source for tracking the pandemic’s impact across countries and regions.
""")
    with col2:
        st.image('https://themwl.org/sites/default/files/who-logo_0.jpg',
                width = 250)
st.header('Application Overview')
st.markdown("""
This tool allows users to explore and analyze Covid-19 statistics 
from different regions and time periods using interactive visualizations and summaries.
""")