"""
Finanzas Familia V&V — Streamlit App
=====================================
Envuelve el dashboard HTML en Streamlit para deployment en streamlit.io

Requisitos:
    pip install streamlit

Correr localmente:
    streamlit run streamlit_app.py

Subir a Streamlit Cloud:
    1. Sube este archivo + finanzas_vv_dashboard.html al mismo repo de GitHub
    2. Ve a share.streamlit.io → New app → conecta tu repo
    3. Main file: streamlit_app.py
"""

import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Finanzas Familia V&V",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Quitar padding por defecto de Streamlit para que el dashboard ocupe todo
st.markdown("""
<style>
    .stApp { background: #0b1929; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none; }
    section[data-testid="stSidebar"] { display: none; }
    footer { display: none; }
</style>
""", unsafe_allow_html=True)

# Cargar el HTML del dashboard
html_file = os.path.join(os.path.dirname(__file__), "finanzas_vv_dashboard.html")

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error("⚠️ No se encontró `finanzas_vv_dashboard.html`. "
             "Asegúrate de que esté en el mismo directorio que este archivo.")
    st.info("Estructura esperada:\n```\ntu-repo/\n  ├── streamlit_app.py\n  └── finanzas_vv_dashboard.html\n```")
