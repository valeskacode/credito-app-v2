import streamlit as st
import pandas as pd


def render():

    st.subheader("🔍 Búsqueda de Cliente")

    # =====================================
    # Validar Excel cargado
    # =====================================

    if (
        "df_clientes" not in st.session_state
        or st.session_state.df_clientes is None
    ):

        st.warning(
            "Primero debe cargar el archivo Excel."
        )

        return

    df = st.session_state.df_clientes

    # =====================================
    # Validar columnas disponibles
    # =====================================

    columnas_busqueda = []

    posibles = [
        "DOCPEN",
        "CLIENTE",
        "CODCLI",
        "CODCRE",
        "AGENCIA",
        "ANALISTA"
    ]

    for col in posibles:

        if col in df.columns:

            columnas_busqueda.append(col)

    if len(columnas_busqueda) == 0:

        st.error(
            "No se encontraron columnas válidas para búsqueda."
        )

        st.write(df.columns.tolist())

        return

    # =====================================
    # Inicializar resultados
    # =====================================

    if "resultado_busqueda" not in st.session_state:

        st.session_state.resultado_busqueda = pd.DataFrame()

    # =====================================
    # Formulario
    # =====================================

    with st.form("form_busqueda"):

        col1, col2 = st.columns([1, 3])

        with col1:

            criterio = st.selectbox(
                "Buscar por",
                columnas_busqueda
            )

        with col2:

            valor = st.text_input(
                "Ingrese valor"
            )

        buscar = st.form_submit_button(
            "🔎 Buscar",
            use_container_width=True
        )

    # =====================================
    # Buscar
    # =====================================

    if buscar:

        if not valor:

            st.warning(
                "Ingrese un valor para buscar."
            )

        else:

            try:

                resultado = df[
                    df[criterio]
                    .astype(str)
                    .fillna("")
                    .str.contains(
                        str(valor),
                        case=False,
                        na=False
                    )
                ]

                st.session_state.resultado_busqueda = resultado

            except Exception as e:

                st.error(
                    f"Error en búsqueda: {e}"
                )

    # =====================================
    # Resultados
    # =====================================

    resultado = st.session_state.resultado_busqueda

    if not resultado.empty:

        st.success(
            f"{len(resultado)} registro(s) encontrado(s)"
        )

        for idx, row in resultado.head(30).iterrows():

            with st.container(border=True):

                st.markdown(
                    f"### 👤 {row.get('CLIENTE','SIN NOMBRE')}"
                )

                c1, c2 = st.columns(2)

                with c1:

                    if "DOCPEN" in row.index:

                        st.write(
                            f"**Documento:** {row.get('DOCPEN','')}"
                        )

                    st.write(
                        f"**Código Cliente:** {row.get('CODCLI','')}"
                    )

                    st.write(
                        f"**Código Crédito:** {row.get('CODCRE','')}"
                    )

                with c2:

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
                    "Seleccionar Cliente",
                    key=f"sel_{idx}"
                ):

                    st.session_state.cliente_actual = (
                        row.to_dict()
                    )

                    st.success(
                        "Cliente seleccionado correctamente."
                    )

                    st.rerun()

    elif buscar:

        st.warning(
            "No se encontraron coincidencias."
        )

    # =====================================
    # Cliente activo
    # =====================================

    if st.session_state.get("cliente_actual"):

        cliente = st.session_state.cliente_actual

        st.divider()

        st.success(
            f"Cliente activo: {cliente.get('CLIENTE','')}"
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            if "DOCPEN" in cliente:

                st.metric(
                    "Documento",
                    cliente.get("DOCPEN", "")
                )

        with c2:

            st.metric(
                "Cod. Cliente",
                cliente.get("CODCLI", "")
            )

        with c3:

            st.metric(
                "Cod. Crédito",
                cliente.get("CODCRE", "")
            )

        with st.expander(
            "Ver información completa"
        ):

            st.json(cliente)
