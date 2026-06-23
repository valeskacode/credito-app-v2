import streamlit as st
import pandas as pd


def render():

    st.subheader("🔍 Búsqueda de Cliente")

    # ---------------------------------
    # Validar base cargada
    # ---------------------------------

    if (
        "df_clientes" not in st.session_state
        or st.session_state.df_clientes is None
    ):

        st.warning(
            "Primero debe cargar el Excel desde la pantalla principal."
        )

        return

    df = st.session_state.df_clientes

    # ---------------------------------
    # Inicializar resultados
    # ---------------------------------

    if "resultado_busqueda" not in st.session_state:
        st.session_state.resultado_busqueda = pd.DataFrame()

    # ---------------------------------
    # Formulario de búsqueda
    # ---------------------------------

    with st.form("frm_busqueda"):

        col1, col2 = st.columns([1, 3])

        with col1:

            criterio = st.selectbox(
                "Buscar por",
                [
                    "DOCPEN",
                    "CLIENTE",
                    "CODCLI",
                    "CODCRE"
                ]
            )

        with col2:

            valor = st.text_input(
                "Ingrese búsqueda"
            )

        buscar = st.form_submit_button(
            "🔎 Buscar Cliente",
            use_container_width=True
        )

    # ---------------------------------
    # Ejecutar búsqueda
    # ---------------------------------

    if buscar:

        if not valor:

            st.warning(
                "Ingrese un valor para buscar."
            )

        else:

            try:

                if criterio not in df.columns:

                    st.error(
                        f"La columna '{criterio}' no existe en el Excel."
                    )

                else:

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
                    f"Error durante la búsqueda: {e}"
                )

    # ---------------------------------
    # Mostrar resultados
    # ---------------------------------

    resultado = st.session_state.resultado_busqueda

    if not resultado.empty:

        st.caption(
            f"{len(resultado)} registro(s) encontrado(s)"
        )

        for idx, row in resultado.head(30).iterrows():

            with st.container(border=True):

                st.markdown(
                    f"### {row.get('CLIENTE', '')}"
                )

                c1, c2 = st.columns(2)

                with c1:

                    st.write(
                        f"**DNI:** {row.get('DOCPEN', '')}"
                    )

                    st.write(
                        f"**Código Cliente:** {row.get('CODCLI', '')}"
                    )

                    st.write(
                        f"**Crédito:** {row.get('CODCRE', '')}"
                    )

                with c2:

                    st.write(
                        f"**Agencia:** {row.get('AGENCIA', '')}"
                    )

                    st.write(
                        f"**Saldo:** {row.get('SALDO_MN', '')}"
                    )

                    st.write(
                        f"**Estado:** {row.get('ESTADO_CREDITO', '')}"
                    )

                if st.button(
                    "Seleccionar Cliente",
                    key=f"cliente_{idx}"
                ):

                    st.session_state.cliente_actual = (
                        row.to_dict()
                    )

                    st.success(
                        f"Cliente seleccionado: {row.get('CLIENTE', '')}"
                    )

                    st.rerun()

    elif buscar:

        st.warning(
            "No se encontraron coincidencias."
        )

    # ---------------------------------
    # Cliente seleccionado
    # ---------------------------------

    if st.session_state.get("cliente_actual"):

        cliente = st.session_state.cliente_actual

        st.divider()

        st.success(
            f"Cliente activo: {cliente.get('CLIENTE', '')}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "DNI",
                cliente.get("DOCPEN", "")
            )

        with col2:
            st.metric(
                "Cliente",
                cliente.get("CODCLI", "")
            )

        with col3:
            st.metric(
                "Crédito",
                cliente.get("CODCRE", "")
            )
