import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from day_pages import day8, day9, default_page

st.title('isaman.streamlit')
st.header('30 day of Streamlit')


pages = {
    "Default" :  default_page.page,
    "Day 8" : day8.page,
    "Day 9" : day9.page,
}
page = st.selectbox('Select Page',tuple(pages.keys()))

pages[page]()







