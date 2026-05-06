import streamlit as st
import os

st.set_page_config(
    page_title="Mapa Interativo",
    page_icon="🗺️",
    layout="wide",
)

# ── Minimal dark styling ──────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Syne', sans-serif;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }
    .map-title {
        font-size: 1.6rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0.25rem;
    }
    .map-subtitle {
        font-size: 0.85rem;
        opacity: 0.55;
        margin-bottom: 1.2rem;
    }
    .stAlert {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="map-title">🗺️ Mapa Interativo</div>', unsafe_allow_html=True)
st.markdown('<div class="map-subtitle">Visualização geoespacial — mapa_novo.html</div>', unsafe_allow_html=True)

# ── Load and render the HTML map ──────────────────────────────────────────────
MAP_FILE = "mapa_novo.html"

if os.path.exists(MAP_FILE):
    with open(MAP_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=1250, scrolling=False)

else:
    st.error(
        f"**Arquivo `{MAP_FILE}` não encontrado.**\n\n"
        "Certifique-se de que o arquivo está na mesma pasta que `app.py`."
    )
    st.info(
        "📁 Estrutura esperada:\n"
        "```\n"
        "seu-repositorio/\n"
        "├── app.py\n"
        "├── mapa_novo.html\n"
        "└── requirements.txt\n"
        "```"
    )
