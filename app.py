import streamlit as st
import pandas as pd
import importlib.util
from pathlib import Path

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Evaluación de Crédito",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "paso" not in st.session_state:
    st.session_state.paso = 1

if "df_clientes" not in st.session_state:
    st.session_state.df_clientes = None

if "cliente_actual" not in st.session_state:
    st.session_state.cliente_actual = None

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# =====================================================
# CARGA EXCEL
# =====================================================

@st.cache_data(show_spinner=False)
def cargar_excel(archivo):

    df = pd.read_excel(
        archivo,
        sheet_name="MUESTRA_FINAL",
        dtype=str
    )

    # Limpieza columnas
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.upper()
    )

    return df

# =====================================================
# CARGA DE MÓDULOS
# =====================================================

BASE_DIR = Path(__file__).parent

MODULOS = {
    1: "pages/01_Busqueda.py",
    2: "pages/02_Evaluacion_Credito.py",
    3: "pages/03_Ficha_Cliente.py",
    4: "pages/04_Ingresos_Gastos.py",
    5: "pages/05_Ubicacion.py",
    6: "pages/06_Reporte.py"
}

def cargar_modulo(ruta):

    archivo = BASE_DIR / ruta

    spec = importlib.util.spec_from_file_location(
        archivo.stem,
        archivo
    )

    modulo = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(modulo)

    return modulo

# =====================================================
# HEADER
# =====================================================

st.title("🏦 Sistema de Evaluación Crediticia")

# =====================================================
# USUARIO
# =====================================================

col1, col2 = st.columns([3, 1])

with col1:

    usuario = st.text_input(
        "Usuario",
        value=st.session_state.usuario
    )

with col2:

    if st.button("Guardar Usuario"):

        st.session_state.usuario = usuario

        st.success(
            f"Usuario registrado: {usuario}"
        )

# =====================================================
# CARGA DE EXCEL
# =====================================================

st.markdown("## 📂 Base de Clientes")

archivo = st.file_uploader(
    "Seleccione archivo Excel",
    type=["xlsx"]
)

if archivo is not None:

    try:

        df = cargar_excel(archivo)

        st.session_state.df_clientes = df

        st.success(
            f"Excel cargado correctamente. Registros: {len(df):,}"
        )

        with st.expander("Ver columnas detectadas"):

            st.write(df.columns.tolist())

    except Exception as e:

        st.error(
            f"Error al cargar Excel: {e}"
        )

# =====================================================
# MENÚ
# =====================================================

st.markdown("---")

pasos = {
    1: "Búsqueda",
    2: "Evaluación",
    3: "Ficha Cliente",
    4: "Ingresos y Gastos",
    5: "Ubicación",
    6: "Reporte"
}

st.progress(st.session_state.paso / 6)

st.caption(
    f"Paso {st.session_state.paso} de 6 - "
    f"{pasos[st.session_state.paso]}"
)

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("🔍"):
        st.session_state.paso = 1
        st.rerun()

with c2:
    if st.button("📊"):
        st.session_state.paso = 2
        st.rerun()

with c3:
    if st.button("👤"):
        st.session_state.paso = 3
        st.rerun()

with c4:
    if st.button("💰"):
        st.session_state.paso = 4
        st.rerun()

with c5:
    if st.button("📍"):
        st.session_state.paso = 5
        st.rerun()

with c6:
    if st.button("📄"):
        st.session_state.paso = 6
        st.rerun()

st.markdown("---")

# =====================================================
# EJECUTAR MÓDULO
# =====================================================

try:

    modulo = cargar_modulo(
        MODULOS[st.session_state.paso]
    )

    modulo.render()

except Exception as e:

    st.error(
        f"Error cargando módulo: {e}"
    )

# =====================================================
# NAVEGACIÓN
# =====================================================

st.markdown("---")

b1, b2 = st.columns(2)

with b1:

    if st.button(
        "⬅ Anterior",
        use_container_width=True
    ):

        if st.session_state.paso > 1:

            st.session_state.paso -= 1

            st.rerun()

with b2:

    if st.button(
        "Siguiente ➡",
        use_container_width=True
    ):

        if st.session_state.paso < 6:

            st.session_state.paso += 1

            st.rerun()

# =====================================================
# CLIENTE ACTIVO
# =====================================================

if st.session_state.get("cliente_actual"):

    cliente = st.session_state.cliente_actual

    st.sidebar.success(
        cliente.get("CLIENTE", "")
    )

    st.sidebar.write(
        f"DNI: {cliente.get('DOCPEN','')}"
    )

    st.sidebar.write(
        f"Crédito: {cliente.get('CODCRE','')}"
    )

    st.sidebar.write(
        f"Agencia: {cliente.get('AGENCIA','')}"
    )
