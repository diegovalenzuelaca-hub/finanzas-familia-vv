"""
Finanzas Familia V&V — Streamlit App
Deployment: share.streamlit.io
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

# ── Estilos globales ─────────────────────────────────────────────
st.markdown("""
<style>
    .stApp { background: #0b1929; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header[data-testid="stHeader"] { display: none; }
    section[data-testid="stSidebar"] { display: none; }
    footer { display: none; }
    /* Login */
    .login-wrap {
        max-width: 380px; margin: 8vh auto 0; padding: 2.5rem 2rem;
        background: #112338; border: 1px solid #1d3555; border-radius: 16px; text-align: center;
    }
    .login-wrap h2 { color: #e8f4ff; margin-bottom: .25rem; }
    .login-wrap p  { color: #7fa0c4; font-size: .9rem; margin-bottom: 1.5rem; }
</style>
""", unsafe_allow_html=True)

# ── Contraseña ───────────────────────────────────────────────────
def check_password() -> bool:
    """Devuelve True si el usuario ya está autenticado."""
    if st.session_state.get("authenticated"):
        return True

    st.markdown("""
    <div class="login-wrap">
        <div style="font-size:3rem">💰</div>
        <h2>Finanzas Familia V&V</h2>
        <p>Dashboard privado · ingresa la contras