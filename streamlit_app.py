import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Finanzas Familia VV",
    page_icon="=",
    layout="wide",
    initial_sidebar_state="collapsed",
)

css = (
    "<style>"
    ".stApp{background:#0b1929}"
    ".block-container{padding:0!important;max-width:100%!important}"
    "header[data-testid='stHeader']{display:none}"
    "section[data-testid='stSidebar']{display:none}"
    "footer{display:none}"
    "</style>"
)
st.markdown(css, unsafe_allow_html=True)

GITHUB_PAGES_URL = "https://diegovalenzuelaca-hub.github.io/finanzas-familia-vv/"


def check_password():
    if st.session_state.get("auth"):
        return True

    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        card = (
            "<div style='background:#112338;border:1px solid #1d3555;"
            "border-radius:16px;padding:2.5rem 2rem;text-align:center'>"
            "<div style='font-size:3rem'>&#128176;</div>"
            "<h2 style='color:#e8f4ff;margin:.5rem 0 .25rem'>Finanzas Familia V&amp;V</h2>"
            "<p style='color:#7fa0c4;font-size:.9rem;margin-bottom:1.5rem'>Dashboard privado</p>"
            "</div>"
        )
        st.markdown(card, unsafe_allow_html=True)
        pwd = st.text_input("pwd", type="password",
                            label_visibility="collapsed",
                            placeholder="Contrasena...")
        if st.button("Entrar", use_container_width=True):
            ok = st.secrets.get("password", "familiaVV2025")
            if pwd == ok:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Contrasena incorrecta.")
    return False


if not check_password():
    st.stop()

# Login OK — cargar el dashboard desde GitHub Pages
components.iframe(GITHUB_PAGES_URL, height=1050, scrolling=True)
