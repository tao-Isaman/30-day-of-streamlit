import os

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from short_page import make_day_page

arr = os.listdir('./day_pages')

st.title('isaman.streamlit')
st.header('30 day of Streamlit')

pages = make_day_page()
page = st.selectbox('Select Page',tuple(pages.keys()))

pages[page]()







