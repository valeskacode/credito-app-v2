import streamlit as st
import pandas as pd
import importlib.util
import traceback
from pathlib import Path

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Evaluación Crediticia",
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
# FUNCIONES
# =====================================================

@st.cache_data(show_spinner=False)
def cargar_excel(archivo):

    df = pd.read_excel(
        archivo,
        sheet_name="MUESTRA_FINAL",
        dtype=str
    )

    # Limpiar nombres de columnas
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.upper()
    )

    return df


def cargar_modulo(ruta):

    archivo = Path(ruta)

    spec = importlib.util.spec_from_file_location(
        archivo.stem,
        archivo
    )

    modulo = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(modulo)

    return modulo

# =====================================================
# CABECERA
# =====================================================

st.title("🏦 Sistema de Evaluación Crediticia")

# =====================================================
# USUARIO
# =====================================================

with st.container(border=True):

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

st.markdown("## 📂 Cargar Base de Clientes")

archivo = st.file_uploader(
    "Seleccione archivo Excel",
    type=["xlsx"]
)

if archivo:

    try:

        df = cargar_excel(archivo)

        st.session_state.df_clientes = df

        st.success(
            f"Base cargada correctamente: {len(df):,} registros"
        )

        # =====================================
        # DIAGNÓSTICO DE COLUMNAS
        # =====================================

        with st.expander("🔍 Diagnóstico de Columnas"):

            st.write(
                "Columnas encontradas en MUESTRA_FINAL"
            )

            for i, col in enumerate(df.columns):

                st.write(
                    f"{i} -> {repr(col)}"
                )

        # Vista previa

        with st.expander("📄 Vista previa"):

            st.dataframe(
                df.head(5),
                use_container_width=True
            )

    except Exception as e:

        st.error(
            f"Error al leer MUESTRA_FINAL: {e}"
        )

# =====================================================
# PASOS
# =====================================================

pasos = {
    1: "🔍 Búsqueda",
    2: "📊 Evaluación Crédito",
    3: "👤 Ficha Cliente",
    4: "💰 Ingresos y Gastos",
    5: "📍 Ubicación",
    6: "📄 Reporte"
}

st.markdown("---")

st.progress(
    st.session_state.paso / 6
)

st.caption(
    f"Paso {st.session_state.paso} de 6 - "
    f"{pasos[st.session_state.paso]}"
)

# =====================================================
# MENÚ
# =====================================================

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("🔍 Buscar"):
        st.session_state.paso = 1
        st.rerun()

with c2:
    if st.button("📊 Crédito"):
        st.session_state.paso = 2
        st.rerun()

with c3:
    if st.button("👤 Cliente"):
        st.session_state.paso = 3
        st.rerun()

with c4:
    if st.button("💰 Ingresos"):
        st.session_state.paso = 4
        st.rerun()

with c5:
    if st.button("📍 Ubicación"):
        st.session_state.paso = 5
        st.rerun()

with c6:
    if st.button("📄 Reporte"):
        st.session_state.paso = 6
        st.rerun()

st.markdown("---")

# =====================================================
# RUTAS
# =====================================================

modulos = {
    1: "pages/01_Busqueda.py",
    2: "pages/02_Evaluacion_Credito.py",
    3: "pages/03_Ficha_Cliente.py",
    4: "pages/04_Ingresos_Gastos.py",
    5: "pages/05_Ubicacion.py",
    6: "pages/06_Reporte.py"
}

# =====================================================
# EJECUTAR MÓDULO
# =====================================================

try:

    ruta = modulos[
        st.session_state.paso
    ]

    modulo = cargar_modulo(ruta)

    modulo.render()

except Exception as e:

    st.error(
        f"Error cargando módulo: {str(e)}"
    )

    st.code(
        traceback.format_exc()
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

if st.session_state.get(
    "cliente_actual"
):

    cliente = st.session_state.cliente_actual

    st.sidebar.success(
        "Cliente Seleccionado"
    )

    st.sidebar.write(
        cliente.get(
            "CLIENTE",
            ""
        )
    )

    if "DOCPEN" in cliente:

        st.sidebar.write(
            f"DNI: {cliente.get('DOCPEN','')}"
        )

    st.sidebar.write(
        f"Cod Cliente: {cliente.get('CODCLI','')}"
    )

    st.sidebar.write(
        f"Crédito: {cliente.get('CODCRE','')}"
    )
