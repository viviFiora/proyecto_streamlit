import streamlit as st
import pandas as pd

datos = pd.read_csv("clientes.csv")

st.title("Clientes Registrados")
st.divider()
st.data_editor(datos)

editar_datos = st.button("Guardar datos alterados")
if editar_datos:
    datos.to_csv("clientes.csv", index=False,)
    st.success("Datos alterados con suceso!!")