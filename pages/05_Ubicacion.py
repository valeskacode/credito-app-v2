import streamlit as st
from datetime import datetime


def render():

    st.subheader("📍 Ubicación y Verificación de Visita")

    cliente = st.session_state.get(
        "cliente_actual"
    )

    if not cliente:

        st.warning(
            "Debe seleccionar un cliente."
        )

        return

    # ----------------------------------
    # Inicializar
    # ----------------------------------

    if "ubicacion_visita" not in st.session_state:

        st.session_state.ubicacion_visita = {}

    data = st.session_state.ubicacion_visita

    # ----------------------------------
    # DATOS DEL CLIENTE
    # ----------------------------------

    st.markdown("## Cliente")

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

    with col2:

        st.text_input(
            "Código Cliente",
            value=cliente.get(
                "CODCLI",
                ""
            ),
            disabled=True
        )

        st.text_input(
            "Código Crédito",
            value=cliente.get(
                "CODCRE",
                ""
            ),
            disabled=True
        )

    st.divider()

    # ----------------------------------
    # DOMICILIO
    # ----------------------------------

    st.markdown("## Domicilio")

    st.text_area(
        "Dirección registrada",
        value=cliente.get(
            "DIRECCION_DOM",
            ""
        ),
        disabled=True
    )

    data["domicilio_confirmado"] = st.checkbox(
        "Domicilio confirmado",
        value=data.get(
            "domicilio_confirmado",
            False
        )
    )

    st.divider()

    # ----------------------------------
    # NEGOCIO
    # ----------------------------------

    st.markdown("## Negocio")

    st.text_area(
        "Dirección del negocio",
        value=cliente.get(
            "DIRECCION_NEG",
            ""
        ),
        disabled=True
    )

    data["negocio_confirmado"] = st.checkbox(
        "Negocio confirmado",
        value=data.get(
            "negocio_confirmado",
            False
        )
    )

    st.divider()

    # ----------------------------------
    # GEOLOCALIZACIÓN
    # ----------------------------------

    st.markdown("## Geolocalización")

    data["latitud"] = st.text_input(
        "Latitud",
        value=data.get(
            "latitud",
            ""
        )
    )

    data["longitud"] = st.text_input(
        "Longitud",
        value=data.get(
            "longitud",
            ""
        )
    )

    st.info(
        "En una siguiente versión puede integrarse captura automática GPS."
    )

    st.divider()

    # ----------------------------------
    # FOTOS
    # ----------------------------------

    st.markdown("## Evidencias Fotográficas")

    foto_fachada = st.file_uploader(
        "Foto fachada",
        type=["jpg", "jpeg", "png"]
    )

    foto_negocio = st.file_uploader(
        "Foto negocio",
        type=["jpg", "jpeg", "png"]
    )

    foto_cliente = st.file_uploader(
        "Foto cliente",
        type=["jpg", "jpeg", "png"]
    )

    data["foto_fachada"] = (
        foto_fachada.name
        if foto_fachada
        else ""
    )

    data["foto_negocio"] = (
        foto_negocio.name
        if foto_negocio
        else ""
    )

    data["foto_cliente"] = (
        foto_cliente.name
        if foto_cliente
        else ""
    )

    st.divider()

    # ----------------------------------
    # REFERENCIAS
    # ----------------------------------

    st.markdown("## Referencias de Ubicación")

    data["referencias"] = st.text_area(
        "Referencias para llegar",
        value=data.get(
            "referencias",
            ""
        ),
        height=100
    )

    st.divider()

    # ----------------------------------
    # RESULTADO DE VISITA
    # ----------------------------------

    st.markdown("## Resultado")

    data["resultado_visita"] = st.selectbox(
        "Resultado de visita",
        [
            "EXITOSA",
            "OBSERVADA",
            "NO UBICADO",
            "NEGOCIO CERRADO"
        ],
        index=[
            "EXITOSA",
            "OBSERVADA",
            "NO UBICADO",
            "NEGOCIO CERRADO"
        ].index(
            data.get(
                "resultado_visita",
                "EXITOSA"
            )
        )
    )

    data["fecha_visita"] = str(
        datetime.now()
    )

    st.divider()

    # ----------------------------------
    # OBSERVACIONES
    # ----------------------------------

    data["observaciones_visita"] = st.text_area(
        "Observaciones",
        value=data.get(
            "observaciones_visita",
            ""
        ),
        height=150
    )

    # ----------------------------------
    # GUARDAR
    # ----------------------------------

    st.session_state.ubicacion_visita = data

    st.success(
        "Información de visita actualizada."
    )

    # ----------------------------------
    # RESUMEN
    # ----------------------------------

    with st.expander(
        "Ver información registrada"
    ):

        st.json(
            st.session_state.ubicacion_visita
        )
