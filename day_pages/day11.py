import streamlit as st

def page():
    st.header('st.multiselect')
    
    options = st.multiselect(
         'What are your favorite colors',
         ['Green', 'Yellow', 'Red', 'Blue'],
         ['Yellow', 'Red'])
    
    st.write('You selected:', options)