import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from streamlit_pandas_profiling import st_profile_report


add_radio = st.radio("Seleccione el formato",("CSV", "EXCEL","JSON"))
if add_radio == "CSV" or add_radio == "EXCEL":
    file = st.file_uploader("Seleccione el archivo")
if add_radio == "JSON":
    title = st.text_input("Ingresa la URL aquí 👇")
    
@st.cache
def load_data():
    data = pd.read_excel(file)
    return data
df = load_data()

# show data on streamlit
st.write(df)
