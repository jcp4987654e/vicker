import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser lo primero que se ejecute en tu script.
st.set_page_config(
    page_title="Ensayo de Dureza Vickers",
    page_icon="💎",
    layout="wide", # Usa el ancho completo de la página
    initial_sidebar_state="collapsed", # Oculta la barra lateral por defecto
)

# --- CARGAR EL HTML ---
# Abre el archivo HTML que creamos y guárdalo en una variable.
with open('index.html', 'r', encoding='utf-8') as f:
    html_code = f.read()

# --- MOSTRAR EL HTML EN STREAMLIT ---
# Usa st.components.v1.html para renderizar tu código HTML.
# Le damos un alto generoso para que ocupe buena parte de la pantalla y activamos el scroll.
st.components.v1.html(html_code, height=1200, scrolling=True)