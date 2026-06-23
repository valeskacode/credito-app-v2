import streamlit as st


def render():

    st.subheader("📊 Evaluación de Crédito")

    # -----------------------------------
    # Validar cliente seleccionado
    # -----------------------------------

    cliente = st.session_state.get(
        "cliente_actual"
    )

    if not cliente:

        st.warning(
            "Debe seleccionar un cliente en la pantalla de búsqueda."
        )

        return

    # -----------------------------------
    # Inicializar evaluación
    # -----------------------------------

    if "evaluacion_credito" not in st.session_state:

        st.session_state.evaluacion_credito = {}

    evaluacion = st.session_state.evaluacion_credito

    # -----------------------------------
    # Resumen del crédito
    # -----------------------------------

    st.markdown("### Información del Crédito")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Cliente",
            cliente.get("CLIENTE", "")
        )

    with c2:

        st.metric(
            "Crédito",
            cliente.get("CODCRE", "")
        )

    with c3:

        st.metric(
            "Saldo",
            cliente.get("SALDO_MN", "")
        )

    st.divider()

    # -----------------------------------
    # Indicadores de Riesgo
    # -----------------------------------

    st.markdown("### Indicadores")

    col1, col2, col3 = st.columns(3)

    with col1:

        dias_atraso = cliente.get(
            "DIAS_ATRASO",
            "0"
        )

        st.metric(
            "Días Atraso",
            dias_atraso
        )

    with col2:

        st.metric(
            "Tipo SBS",
            cliente.get(
                "TIPO_SBS",
                ""
            )
        )

    with col3:

        st.metric(
            "Categoría",
            cliente.get(
                "CATEG_RESULTANTE",
                ""
            )
        )

    # -----------------------------------
    # Historial de atraso
    # -----------------------------------

    st.markdown("### Historial de Atrasos")

    atraso_cols = [
        "ATRANT_1M",
        "ATRANT_2M",
        "ATRANT_3M",
        "ATRANT_4M",
        "ATRANT_5M",
        "ATRANT_6M"
    ]

    historial = {}

    for col in atraso_cols:

        historial[col] = cliente.get(
            col,
            ""
        )

    st.json(historial)

    st.divider()

    # -----------------------------------
    # Evaluación del Analista
    # -----------------------------------

    st.markdown("### Validaciones")

    evaluacion["documentacion_correcta"] = st.checkbox(
        "Documentación completa",
        value=evaluacion.get(
            "documentacion_correcta",
            False
        )
    )

    evaluacion["actividad_confirmada"] = st.checkbox(
        "Actividad económica confirmada",
        value=evaluacion.get(
            "actividad_confirmada",
            False
        )
    )

    evaluacion["domicilio_confirmado"] = st.checkbox(
        "Domicilio confirmado",
        value=evaluacion.get(
            "domicilio_confirmado",
            False
        )
    )

    evaluacion["negocio_operativo"] = st.checkbox(
        "Negocio operativo",
        value=evaluacion.get(
            "negocio_operativo",
            False
        )
    )

    evaluacion["cliente_contactado"] = st.checkbox(
        "Cliente contactado",
        value=evaluacion.get(
            "cliente_contactado",
            False
        )
    )

    st.divider()

    # -----------------------------------
    # Riesgo Percibido
    # -----------------------------------

    st.markdown("### Riesgo Percibido")

    evaluacion["riesgo"] = st.radio(
        "Nivel de riesgo",
        [
            "BAJO",
            "MEDIO",
            "ALTO"
        ],
        index=[
            "BAJO",
            "MEDIO",
            "ALTO"
        ].index(
            evaluacion.get(
                "riesgo",
                "MEDIO"
            )
        )
    )

    # -----------------------------------
    # Recomendación
    # -----------------------------------

    st.markdown("### Recomendación")

    evaluacion["recomendacion"] = st.selectbox(
        "Resultado",
        [
            "FAVORABLE",
            "OBSERVADO",
            "DESFAVORABLE"
        ],
        index=[
            "FAVORABLE",
            "OBSERVADO",
            "DESFAVORABLE"
        ].index(
            evaluacion.get(
                "recomendacion",
                "FAVORABLE"
            )
        )
    )

    # -----------------------------------
    # Observaciones
    # -----------------------------------

    st.markdown("### Observaciones")

    evaluacion["observaciones"] = st.text_area(
        "Comentarios del analista",
        value=evaluacion.get(
            "observaciones",
            ""
        ),
        height=150
    )

    # -----------------------------------
    # Guardar
    # -----------------------------------

    st.session_state.evaluacion_credito = evaluacion

    st.success(
        "Evaluación actualizada."
    )

    # -----------------------------------
    # Resumen
    # -----------------------------------

    with st.expander(
        "Ver evaluación registrada"
    ):

        st.json(
            st.session_state.evaluacion_credito
        )
