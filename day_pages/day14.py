import streamlit as st 
import pandas as pd
from streamlit_pandas_profiling import st_profile_report

def page():
    st.header('Streamlit Components')
    

    st.title('`streamlit_pandas_profiling`')

    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

    pr = df.profile_report()
    st_profile_report(pr)
    
    