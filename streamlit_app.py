import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report

with st.sidebar:
    st.title("Menu principal")
    add_radio = st.radio("Seleccione el formato",("CSV", "EXCEL","JSON"))
    
    @st.cache
    def load_data():
        if add_radio == "CSV":
            file = st.file_uploader("Seleccione el archivo")
            df = pd.read_csv(file)
        if add_radio == "EXCEL":
            file = st.file_uploader("Seleccione el archivo")
            df = pd.read_excel(file)
        if add_radio == "JSON":
            title = st.text_input("Ingresa la URL aquí 👇")
            df = pd.read_json(title)
        return df
    df = load_data()

st.title("Perfilamiento de datos ")
try:
    pr = df.profile_report()
    st_profile_report(pr)
except:
    pass
