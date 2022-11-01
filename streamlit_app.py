import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report

with st.sidebar:
    st.title("Menu principal")
    add_radio = st.selectbox("Seleccione el formato",("CSV", "EXCEL","JSON")
    if add_radio == "CSV" or add_radio == "EXCEL":
        file = st.file_uploader("Seleccione el archivo")
    if add_radio == "JSON":
        title = st.text_input("Ingresa la URL aquí 👇")                         
    @st.cache(persist=True)
    def load_data():
        if add_radio == "CSV":
            df = pd.read_csv(file)
        if add_radio == "EXCEL":
            df = pd.read_excel(file)
        if add_radio == "JSON":
            df = pd.read_json(title)
        return df
    df = load_data()

st.title("Perfilamiento de datos ")
try:
    pr = df.profile_report()
    st_profile_report(pr)
except:
    pass
