import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from streamlit_pandas_profiling import st_profile_report



file = st.file_uploader("Seleccione el archivo")
@st.cache
def load_data():
    data = pd.read_excel(file)
    return data
df = load_data()

# show data on streamlit
st.write(df)
