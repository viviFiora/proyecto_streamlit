import streamlit as st
import pandas as pd
from datetime import date

def guardar_datos(nombre, fecha_nac, tipo_cliente, sexo, edad):
    if nombre and fecha_nac <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nombre},{fecha_nac},{tipo_cliente},{sexo},{edad}\n")
        st.session_state["exito"] = True
    else:
        st.session_state["exito"] = False


st.set_page_config(
    page_title="Registro de Clientes",
    page_icon="📓"
)

st.title("Registro de Clientes")
st.divider()

nombre = st.text_input("Ingrese el nombre del cliente",
                       key="nombre_cliente")

fecha_nac = st.date_input("Fecha de nacimiento",
                           format="DD/MM/YYYY")

sexo = st.radio("Seleccione el sexo del cliente",
                options=["Masculino", "Femenino"])

edad = st.number_input("Ingrese la edad del cliente: ",
                       key="n"
                       "umber_edad",
                       min_value=0,
                       max_value=180)

tipo_cliente = st.selectbox("Tipo de cliente",
                            ["Persona Juridica", "Persona Fisica"])

btn_registro = st.button("Registrar", 
                        on_click=guardar_datos,
                        args=[nombre, fecha_nac, tipo_cliente, sexo, edad])

if btn_registro:
    if st.session_state["exito"]:
        st.success("Cliente registrado con suceso!",
                   icon="✅")
    else:
        st.error("Existe algun error en el registro del cliente",
                 icon="❌")
        
