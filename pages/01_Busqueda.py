import streamlit as st
import pandas as pd


def render():

    st.subheader("🔍 Búsqueda de Cliente")

    # -----------------------------
    # Validar base cargada
    # -----------------------------

    if "df_clientes" not in st.session_state:

        st.warning(
            "Primero debe cargar el Excel."
        )

        return

    df = st.session_state.df_clientes

    # -----------------------------
    # Filtros
    # -----------------------------

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

    # -----------------------------
    # Sin búsqueda
    # -----------------------------

    if not valor:

        st.info(
            "Ingrese un valor para buscar."
        )

        return

    # -----------------------------
    # Filtrar
    # -----------------------------

    resultado = df[
        df[criterio]
        .fillna("")
        .astype(str)
        .str.contains(
            valor,
            case=False,
            na=False
        )
    ]

    st.caption(
        f"{len(resultado)} registro(s) encontrado(s)"
    )

    # -----------------------------
    # Sin resultados
    # -----------------------------

    if resultado.empty:

        st.warning(
            "No se encontraron coincidencias."
        )

        return

    # -----------------------------
    # Resultados
    # -----------------------------

    for idx, row in resultado.head(30).iterrows():

        with st.container(border=True):

            st.markdown(
                f"### {row.get('CLIENTE','')}"
            )

            c1, c2 = st.columns(2)

            with c1:

                st.write(
                    f"**DNI:** {row.get('DOCPEN','')}"
                )

                st.write(
                    f"**Cod Cliente:** {row.get('CODCLI','')}"
                )

                st.write(
                    f"**Crédito:** {row.get('CODCRE','')}"
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
                "Seleccionar",
                key=f"cliente_{idx}"
            ):

                st.session_state.cliente_actual = (
                    row.to_dict()
                )

                st.success(
                    "Cliente seleccionado."
                )

                st.rerun()

    # -----------------------------
    # Cliente activo
    # -----------------------------

    if st.session_state.get(
        "cliente_actual"
    ):

        cliente = (
            st.session_state
            .cliente_actual
        )

        st.divider()

        st.success(
            f"Cliente activo: "
            f"{cliente.get('CLIENTE','')}"
        )

        st.write(
            f"DNI: {cliente.get('DOCPEN','')}"
        )

        st.write(
            f"Crédito: {cliente.get('CODCRE','')}"
        )
