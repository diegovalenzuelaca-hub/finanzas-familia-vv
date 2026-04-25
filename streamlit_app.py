import streamlit as st
import streamlit.components.v1 as components
import requests
import csv
import json
import os
from io import StringIO

st.set_page_config(
    page_title="Finanzas Familia VV",
    page_icon="=",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    "<style>"
    ".stApp{background:#0b1929}"
    ".block-container{padding:0!important;max-width:100%!important}"
    "header[data-testid='stHeader']{display:none}"
    "section[data-testid='stSidebar']{display:none}"
    "footer{display:none}"
    "</style>",
    unsafe_allow_html=True,
)

SHEET_ID = "11I9qygHo_HXBr2BZkyEgVxN8xvb8HE8gD-HMwFZ5Zyo"
SHEETS = {
    "FLUJO":      "Flujo_Caja_Mes",
    "GASTOS":     "Gastos_Mes_Apilado",
    "INGRESOS":   "Ingresos_Mes_Apilado",
    "AHORROS":    "Ahorros_Mes_Apilado",
    "INVERSIONES":"Inversion_Mes_Apilado",
}


def check_password():
    if st.session_state.get("auth"):
        return True
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown(
            "<div style='background:#112338;border:1px solid #1d3555;"
            "border-radius:16px;padding:2.5rem 2rem;text-align:center'>"
            "<div style='font-size:3rem'>&#128176;</div>"
            "<h2 style='color:#e8f4ff;margin:.5rem 0 .25rem'>Finanzas Familia V&amp;V</h2>"
            "<p style='color:#7fa0c4;font-size:.9rem;margin-bottom:1.5rem'>Dashboard privado</p>"
            "</div>",
            unsafe_allow_html=True,
        )
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


@st.cache_data(ttl=1800)
def fetch_all_sheets():
    raw = {}
    for key, name in SHEETS.items():
        url = (
            "https://docs.google.com/spreadsheets/d/"
            + SHEET_ID
            + "/gviz/tq?tqx=out:csv&sheet="
            + name
        )
        try:
            r = requests.get(url, timeout=30)
            reader = csv.DictReader(StringIO(r.text))
            raw[key] = [dict(row) for row in reader]
        except Exception:
            raw[key] = []
    return raw


if not check_password():
    st.stop()

# ── Login OK: fetchear datos en Python e inyectarlos en el HTML ──
with st.spinner("Cargando datos de Google Sheets..."):
    raw_data = fetch_all_sheets()

html_file = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

injection = "<script>var PRE_LOADED_RAW = " + json.dumps(raw_data) + ";</script>"
html_final = html.replace("</head>", injection + "</head>", 1)

components.html(html_final, height=1050, scrolling=True)
