import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- CONFIGURACIÓN DE GOOGLE SHEETS ---
# Sustituye esto por la URL de tu hoja (asegúrate de que termine en /export?format=csv)
SHEET_ID = "TU_ID_DE_LA_HOJA" # Ver nota abajo
URL_HOJA = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.set_page_config(page_title="Reto de Peso 2026", layout="wide")

st.title("🏆 Reto: ¿Quién pierde más?")
st.write("Reto: 18 Feb - 4 May")

# --- FUNCIONES PARA DATOS ---
def leer_datos():
    try:
        # Aquí usamos pandas para leer la hoja pública
        return pd.read_csv(URL_HOJA)
    except:
        return pd.DataFrame(columns=['Fecha', 'Jugador', 'Peso'])

# --- INTERFAZ ---
datos = leer_datos()

with st.sidebar:
    st.header("Registrar Peso")
    fecha = st.date_input("Fecha del lunes", datetime.now())
    jugador = st.selectbox("Jugador", ["Jugador 1", "Jugador 2"])
    peso = st.number_input("Peso actual (kg)", format="%.2f")
    
    if st.button("Guardar Registro"):
        # NOTA: Para escribir en Google Sheets de forma sencilla 
        # lo ideal es usar la librería 'gsheetsdb' o enviar por URL.
        # Por ahora, este botón te mostrará el mensaje:
        st.warning("Para guardar datos automáticamente, necesitamos configurar 'Streamlit Secrets'.")

# --- GRÁFICAS ---
if not datos.empty:
    fig = px.line(datos, x="Fecha", y="Peso", color="Jugador", title="Evolución Semanal")
    st.plotly_chart(fig)
else:
    st.info("Conecta tu hoja de cálculo para ver las gráficas.")
