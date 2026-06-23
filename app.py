import streamlit as st

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Evaluación de Crédito",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# ESTADO DE SESIÓN
# --------------------------------------------------

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if "cliente_actual" not in st.session_state:
    st.session_state.cliente_actual = None

# --------------------------------------------------
# CABECERA
# --------------------------------------------------

st.title("🏦 Evaluación de Crédito")
st.markdown("---")

# --------------------------------------------------
# USUARIO
# --------------------------------------------------

st.subheader("Usuario")

usuario = st.text_input(
    "Ingrese su usuario",
    value=st.session_state.usuario
)

if st.button("Ingresar"):
    st.session_state.usuario = usuario
    st.success(f"Bienvenido {usuario}")

st.markdown("---")

# --------------------------------------------------
# FLUJO DEL PROCESO
# --------------------------------------------------

st.subheader("Flujo de Navegación")

flujo = [
    "🔍 Búsqueda y Carga",
    "📊 Evaluación de Crédito",
    "👤 Ficha del Cliente",
    "💰 Ingresos y Gastos",
    "📍 Ubicación",
    "📄 Reporte"
]

for paso in flujo:
    st.write(paso)

st.markdown("---")

# --------------------------------------------------
# ESTADO
# --------------------------------------------------

if st.session_state.usuario:
    st.success(f"Usuario activo: {st.session_state.usuario}")
else:
    st.warning("Ingrese un usuario para comenzar.")

st.info(
    """
    Esta es la versión inicial del sistema.

    Próximos módulos:
    - Carga de Excel (MUESTRA_FINAL)
    - Búsqueda de clientes
    - Evaluación de crédito
    - Ficha cliente
    - Ingresos y gastos
    - Geolocalización
    - Reporte Word y PDF
    """
)
