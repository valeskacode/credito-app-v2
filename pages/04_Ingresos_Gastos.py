import streamlit as st


def render():

    st.subheader("💰 Ingresos y Gastos")

    cliente = st.session_state.get(
        "cliente_actual"
    )

    if not cliente:

        st.warning(
            "Debe seleccionar un cliente."
        )

        return

    # -----------------------------------
    # Inicializar
    # -----------------------------------

    if "ingresos_gastos" not in st.session_state:

        st.session_state.ingresos_gastos = {}

    data = st.session_state.ingresos_gastos

    # -----------------------------------
    # DATOS DEL NEGOCIO
    # -----------------------------------

    st.markdown("## Información del Negocio")

    c1, c2 = st.columns(2)

    with c1:

        st.text_input(
            "Cliente",
            value=cliente.get(
                "CLIENTE",
                ""
            ),
            disabled=True
        )

    with c2:

        st.text_input(
            "Actividad Económica",
            value=cliente.get(
                "ACTIVIDAD_ECON",
                ""
            ),
            disabled=True
        )

    st.divider()

    # -----------------------------------
    # INGRESOS
    # -----------------------------------

    st.markdown("## Ingresos Mensuales")

    c1, c2 = st.columns(2)

    with c1:

        data["ventas_mensuales"] = st.number_input(
            "Ventas Mensuales",
            min_value=0.0,
            value=float(
                data.get(
                    "ventas_mensuales",
                    0
                )
            ),
            step=100.0
        )

        data["otros_ingresos"] = st.number_input(
            "Otros Ingresos",
            min_value=0.0,
            value=float(
                data.get(
                    "otros_ingresos",
                    0
                )
            ),
            step=100.0
        )

    with c2:

        data["ingreso_conyuge"] = st.number_input(
            "Ingreso Cónyuge",
            min_value=0.0,
            value=float(
                data.get(
                    "ingreso_conyuge",
                    0
                )
            ),
            step=100.0
        )

        data["ingreso_familiar"] = (
            data["ventas_mensuales"]
            + data["otros_ingresos"]
            + data["ingreso_conyuge"]
        )

        st.metric(
            "Ingreso Total",
            f"S/ {data['ingreso_familiar']:,.2f}"
        )

    st.divider()

    # -----------------------------------
    # GASTOS
    # -----------------------------------

    st.markdown("## Gastos Mensuales")

    col1, col2 = st.columns(2)

    with col1:

        data["alimentacion"] = st.number_input(
            "Alimentación",
            min_value=0.0,
            value=float(
                data.get(
                    "alimentacion",
                    0
                )
            )
        )

        data["servicios"] = st.number_input(
            "Servicios Básicos",
            min_value=0.0,
            value=float(
                data.get(
                    "servicios",
                    0
                )
            )
        )

        data["educacion"] = st.number_input(
            "Educación",
            min_value=0.0,
            value=float(
                data.get(
                    "educacion",
                    0
                )
            )
        )

    with col2:

        data["transporte"] = st.number_input(
            "Transporte",
            min_value=0.0,
            value=float(
                data.get(
                    "transporte",
                    0
                )
            )
        )

        data["salud"] = st.number_input(
            "Salud",
            min_value=0.0,
            value=float(
                data.get(
                    "salud",
                    0
                )
            )
        )

        data["otros_gastos"] = st.number_input(
            "Otros Gastos",
            min_value=0.0,
            value=float(
                data.get(
                    "otros_gastos",
                    0
                )
            )
        )

    data["gasto_total"] = (
        data["alimentacion"]
        + data["servicios"]
        + data["educacion"]
        + data["transporte"]
        + data["salud"]
        + data["otros_gastos"]
    )

    st.metric(
        "Gasto Total",
        f"S/ {data['gasto_total']:,.2f}"
    )

    st.divider()

    # -----------------------------------
    # CRÉDITOS VIGENTES
    # -----------------------------------

    st.markdown("## Obligaciones Financieras")

    data["cuota_creditos"] = st.number_input(
        "Cuotas Mensuales de Créditos",
        min_value=0.0,
        value=float(
            data.get(
                "cuota_creditos",
                0
            )
        )
    )

    st.divider()

    # -----------------------------------
    # RESULTADOS
    # -----------------------------------

    st.markdown("## Resultado Financiero")

    data["utilidad_neta"] = (
        data["ingreso_familiar"]
        - data["gasto_total"]
    )

    data["capacidad_pago"] = (
        data["utilidad_neta"]
        - data["cuota_creditos"]
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Utilidad Neta",
            f"S/ {data['utilidad_neta']:,.2f}"
        )

    with c2:

        st.metric(
            "Capacidad de Pago",
            f"S/ {data['capacidad_pago']:,.2f}"
        )

    st.divider()

    # -----------------------------------
    # EVALUACIÓN AUTOMÁTICA
    # -----------------------------------

    if data["capacidad_pago"] > 1000:

        conclusion = "FAVORABLE"

    elif data["capacidad_pago"] > 0:

        conclusion = "OBSERVADO"

    else:

        conclusion = "DESFAVORABLE"

    st.markdown("## Conclusión")

    if conclusion == "FAVORABLE":

        st.success(conclusion)

    elif conclusion == "OBSERVADO":

        st.warning(conclusion)

    else:

        st.error(conclusion)

    data["conclusion_financiera"] = conclusion

    # -----------------------------------
    # OBSERVACIONES
    # -----------------------------------

    data["observaciones_financieras"] = st.text_area(
        "Observaciones Financieras",
        value=data.get(
            "observaciones_financieras",
            ""
        ),
        height=120
    )

    # -----------------------------------
    # GUARDAR
    # -----------------------------------

    st.session_state.ingresos_gastos = data

    st.success(
        "Información financiera actualizada."
    )

    # -----------------------------------
    # RESUMEN
    # -----------------------------------

    with st.expander(
        "Ver información registrada"
    ):

        st.json(
            st.session_state.ingresos_gastos
        )
