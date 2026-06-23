
import streamlit as st

st.set_page_config(page_title="Evaluación Crédito", layout="wide")

st.title("Evaluación de Crédito")
st.write("Plantilla base para GitHub")

flujo = [
    "1. Búsqueda y carga",
    "2. Evaluación crédito",
    "3. Ficha cliente",
    "4. Ingresos y gastos",
    "5. Ubicación",
    "6. Reporte"
]

for paso in flujo:
    st.write(paso)
