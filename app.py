
import streamlit as st

# --------------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------------

st.set_page_config(
    page_title="Evaluación de Crédito",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# ESTADO GLOBAL
# --------------------------------------------------

if "usuario" not in st.session_state:
    st.session_state.usuario = None

if "cliente_actual" not in st.session_state:
    st.session_state.cliente_actual = None

if "evaluacion_actual" not in st.session_state:
    st.session_state.evaluacion_actual = {}

# --------------------------------------------------
# CABECERA
# --------------------------------------------------

st.title("🏦 Evaluación de Crédito")
st.caption("Visitas y evaluación de clientes")

# --------------------------------------------------
# LOGIN SIMPLE
# --------------------------------------------------

with st.sidebar:

    st.subheader("Usuario")

    usuario = st.text_input(
        "Ingrese usuario",
        value=st.session_state.usuario or ""
    )

    if st.button("Ingresar"):
        st.session_state.usuario = usuario
        st.success("Usuario registrado")

# --------------------------------------------------
# VALIDAR USUARIO
# --------------------------------------------------

if not st.session_state.usuario:

    st.info("Ingrese un usuario para continuar.")

    st.stop()

# --------------------------------------------------
# MENÚ PRINCIPAL
# --------------------------------------------------

st.markdown("---")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.page_link(
        "pages/01_Busqueda.py",
        label="🔍 Buscar"
    )

with col2:
    st.page_link(
        "pages/02_Evaluacion_Credito.py",
        label="📊 Crédito"
    )

with col3:
    st.page_link(
        "pages/03_Ficha_Cliente.py",
        label="👤 Cliente"
    )

with col4:
    st.page_link(
        "pages/04_Ingresos_Gastos.py",
        label="💰 Ingresos"
    )

with col5:
    st.page_link(
        "pages/05_Ubicacion.py",
        label="📍 Ubicación"
    )

with col6:
    st.page_link(
        "pages/06_Reporte.py",
        label="📄 Reporte"
    )

# --------------------------------------------------
# PANTALLA PRINCIPAL
# --------------------------------------------------

st.markdown("### Flujo de trabajo")

pasos = [
    "1. Búsqueda y carga",
    "2. Evaluación de crédito",
    "3. Ficha del cliente",
    "4. Ingresos y gastos",
    "5. Ubicación",
    "6. Generación de reporte"
]

for paso in pasos:
    st.write("✅", paso)

st.markdown("---")

st.info(
    f"Usuario activo: {st.session_state.usuario}"
)

if st.session_state.cliente_actual:

    st.success(
        f"Cliente seleccionado: "
        f"{st.session_state.cliente_actual.get('CLIENTE','')}"
    )
else:

    st.warning(
        "Aún no se ha seleccionado un cliente."
    )
```
