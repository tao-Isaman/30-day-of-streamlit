import streamlit as st

def page():
    st.title('st.secrets')

    st.write(st.secrets['message'])