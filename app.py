py -m pip install streamlit-pandas-profiling

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from streamlit_pandas_profiling import st_profile_report




with st.sidebar:
    st.title("Menu principal")
    try:
        add_radio = st.radio("Seleccione el formato",("CSV", "EXCEL","JSON"))
        
        if add_radio == "CSV":
            file = st.file_uploader("Seleccione el archivo")
            df = pd.read_csv(file)
        if add_radio == "EXCEL":
            file = st.file_uploader("Seleccione el archivo")
            df = pd.read_excel(file)
        if add_radio == "JSON":
            title = st.text_input("Ingresa la URL aquí 👇")
            df = pd.read_json(title)
    except:
        pass

st.title("Perfilamiento de datos ")
try:
    pr = df.profile_report()
    st_profile_report(pr)
except:
    pass
