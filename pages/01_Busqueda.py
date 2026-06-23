import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Búsqueda y Carga",
    layout="wide"
)

st.title("🔍 Búsqueda y Carga")

# --------------------------------------------------
# ESTADO
# --------------------------------------------------

if "df_clientes" not in st.session_state:
    st.session_state.df_clientes = None

if "cliente_actual" not in st.session_state:
    st.session_state.cliente_actual = None

# --------------------------------------------------
# CARGAR EXCEL
# --------------------------------------------------

@st.cache_data
def cargar_excel(archivo):
    df = pd.read_excel(
        archivo,
        sheet_name="MUESTRA_FINAL",
        dtype=str
    )

    df.columns = [
        str(c).strip().upper()
        for c in df.columns
    ]

    return df


archivo = st.file_uploader(
    "Seleccione el archivo Excel",
    type=["xlsx"]
)

if archivo:

    try:

        df = cargar_excel(archivo)

        st.session_state.df_clientes = df

        st.success(
            f"Base cargada correctamente ({len(df)} registros)"
        )

    except Exception as e:

        st.error(
            f"Error al leer la hoja MUESTRA_FINAL: {e}"
        )

# --------------------------------------------------
# BUSCADOR
# --------------------------------------------------

if st.session_state.df_clientes is not None:

    st.subheader("Buscar Cliente")

    criterio = st.selectbox(
        "Buscar por",
        [
            "DOCPEN",
            "CLIENTE",
            "CODCLI",
            "CODCRE"
        ]
    )

    valor = st.text_input(
        "Ingrese valor de búsqueda"
    )

    if valor:

        df = st.session_state.df_clientes

        resultado = df[
            df[criterio]
            .fillna("")
            .str.contains(
                valor,
                case=False,
                na=False
            )
        ]

        st.write(
            f"Coincidencias encontradas: {len(resultado)}"
        )

        if len(resultado) > 0:

            for idx, row in resultado.head(50).iterrows():

                with st.container(border=True):

                    st.markdown(
                        f"### {row.get('CLIENTE','')}"
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write(
                            f"**DNI:** {row.get('DOCPEN','')}"
                        )

                        st.write(
                            f"**Cod Cliente:** {row.get('CODCLI','')}"
                        )

                        st.write(
                            f"**Crédito:** {row.get('CODCRE','')}"
                        )

                    with col2:

                        st.write(
                            f"**Agencia:** {row.get('AGENCIA','')}"
                        )

                        st.write(
                            f"**Saldo:** {row.get('SALDO_MN','')}"
                        )

                        st.write(
                            f"**Estado:** {row.get('ESTADO_CREDITO','')}"
                        )

                    if st.button(
                        "Seleccionar",
                        key=f"sel_{idx}"
                    ):

                        st.session_state.cliente_actual = (
                            row.to_dict()
                        )

                        st.success(
                            "Cliente seleccionado"
                        )

                        st.rerun()

# --------------------------------------------------
# CLIENTE SELECCIONADO
# --------------------------------------------------

if st.session_state.cliente_actual:

    st.markdown("---")

    st.subheader("Cliente Actual")

    cliente = st.session_state.cliente_actual

    st.write(
        f"**Cliente:** {cliente.get('CLIENTE','')}"
    )

    st.write(
        f"**DNI:** {cliente.get('DOCPEN','')}"
    )

    st.write(
        f"**Código Cliente:** {cliente.get('CODCLI','')}"
    )

    st.write(
        f"**Código Crédito:** {cliente.get('CODCRE','')}"
    )

    st.info(
        "Ahora puede continuar a la pantalla de Evaluación de Crédito."
    )
