import streamlit as st


def render():

    st.subheader("👤 Ficha del Cliente")

    # ----------------------------------
    # Validar cliente seleccionado
    # ----------------------------------

    cliente = st.session_state.get(
        "cliente_actual"
    )

    if not cliente:

        st.warning(
            "Debe seleccionar un cliente."
        )

        return

    # ----------------------------------
    # Inicializar ficha
    # ----------------------------------

    if "ficha_cliente" not in st.session_state:

        st.session_state.ficha_cliente = {}

    ficha = st.session_state.ficha_cliente

    # ----------------------------------
    # DATOS GENERALES
    # ----------------------------------

    st.markdown("## Datos Generales")

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "Cliente",
            value=cliente.get(
                "CLIENTE",
                ""
            ),
            disabled=True
        )

        st.text_input(
            "DNI",
            value=cliente.get(
                "DOCPEN",
                ""
            ),
            disabled=True
        )

        st.text_input(
            "Código Cliente",
            value=cliente.get(
                "CODCLI",
                ""
            ),
            disabled=True
        )

    with col2:

        st.text_input(
            "Código Crédito",
            value=cliente.get(
                "CODCRE",
                ""
            ),
            disabled=True
        )

        st.text_input(
            "Analista",
            value=cliente.get(
                "ANALISTA",
                ""
            ),
            disabled=True
        )

        st.text_input(
            "Producto",
            value=cliente.get(
                "PRODUCTO_CAJA",
                ""
            ),
            disabled=True
        )

    st.divider()

    # ----------------------------------
    # DOMICILIO
    # ----------------------------------

    st.markdown("## Domicilio")

    st.text_input(
        "Dirección Domicilio",
        value=cliente.get(
            "DIRECCION_DOM",
            ""
        ),
        disabled=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.text_input(
            "Distrito",
            value=cliente.get(
                "DISTRITO_DOM",
                ""
            ),
            disabled=True
        )

    with col2:

        st.text_input(
            "Provincia",
            value=cliente.get(
                "PROVINCIA_DOM",
                ""
            ),
            disabled=True
        )

    with col3:

        st.text_input(
            "Departamento",
            value=cliente.get(
                "DEPARTAMENTO_DOM",
                ""
            ),
            disabled=True
        )

    st.divider()

    # ----------------------------------
    # NEGOCIO
    # ----------------------------------

    st.markdown("## Negocio")

    st.text_input(
        "Actividad Económica",
        value=cliente.get(
            "ACTIVIDAD_ECON",
            ""
        ),
        disabled=True
    )

    st.text_input(
        "Dirección Negocio",
        value=cliente.get(
            "DIRECCION_NEG",
            ""
        ),
        disabled=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.text_input(
            "Distrito Negocio",
            value=cliente.get(
                "DISTRITO_NEG",
                ""
            ),
            disabled=True
        )

    with col2:

        st.text_input(
            "Provincia Negocio",
            value=cliente.get(
                "PROVINCIA_NEG",
                ""
            ),
            disabled=True
        )

    with col3:

        st.text_input(
            "Departamento Negocio",
            value=cliente.get(
                "DEPARTAMENTO_NEG",
                ""
            ),
            disabled=True
        )

    st.divider()

    # ----------------------------------
    # INFORMACIÓN COMPLEMENTARIA
    # ----------------------------------

    st.markdown("## Información de Campo")

    ficha["telefono"] = st.text_input(
        "Teléfono",
        value=ficha.get(
            "telefono",
            ""
        )
    )

    ficha["correo"] = st.text_input(
        "Correo",
        value=ficha.get(
            "correo",
            ""
        )
    )

    ficha["estado_civil"] = st.selectbox(
        "Estado Civil",
        [
            "SOLTERO",
            "CASADO",
            "CONVIVIENTE",
            "DIVORCIADO",
            "VIUDO"
        ],
        index=0
    )

    ficha["numero_hijos"] = st.number_input(
        "Número de Hijos",
        min_value=0,
        value=int(
            ficha.get(
                "numero_hijos",
                0
            )
        )
    )

    ficha["personas_dependen"] = st.number_input(
        "Dependientes",
        min_value=0,
        value=int(
            ficha.get(
                "personas_dependen",
                0
            )
        )
    )

    st.divider()

    # ----------------------------------
    # VALIDACIÓN DE VISITA
    # ----------------------------------

    st.markdown("## Validación de Visita")

    ficha["vive_en_direccion"] = st.checkbox(
        "Vive en dirección declarada",
        value=ficha.get(
            "vive_en_direccion",
            False
        )
    )

    ficha["negocio_operativo"] = st.checkbox(
        "Negocio operativo",
        value=ficha.get(
            "negocio_operativo",
            False
        )
    )

    ficha["cliente_identificado"] = st.checkbox(
        "Cliente identificado",
        value=ficha.get(
            "cliente_identificado",
            False
        )
    )

    ficha["referencias_ok"] = st.checkbox(
        "Referencias verificadas",
        value=ficha.get(
            "referencias_ok",
            False
        )
    )

    st.divider()

    # ----------------------------------
    # OBSERVACIONES
    # ----------------------------------

    ficha["observaciones_cliente"] = st.text_area(
        "Observaciones",
        value=ficha.get(
            "observaciones_cliente",
            ""
        ),
        height=120
    )

    # ----------------------------------
    # GUARDAR
    # ----------------------------------

    st.session_state.ficha_cliente = ficha

    st.success(
        "Ficha actualizada."
    )

    # ----------------------------------
    # RESUMEN
    # ----------------------------------

    with st.expander(
        "Ver ficha registrada"
    ):

        st.json(
            st.session_state.ficha_cliente
        )
