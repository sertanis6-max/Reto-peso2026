import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Reto de Peso 2026", layout="wide")

st.title("🏆 Reto Semanal: ¿Quién pierde más?")
st.subheader("Del 18 de Feb al 4 de Mayo")

# --- LÓGICA DE DATOS ---
# En una app real, usaríamos una base de datos. 
# Para este ejemplo, simulamos los datos de entrada.
if 'datos' not in st.session_state:
    st.session_state.datos = pd.DataFrame(columns=['Fecha', 'Jugador', 'Peso'])

# --- ENTRADA DE DATOS ---
with st.sidebar:
    st.header("Registrar Peso")
    fecha = st.date_input("Fecha del lunes", datetime(2026, 2, 23)) # Primer lunes tras inicio
    jugador = st.selectbox("Jugador", ["Jugador 1", "Jugador 2"])
    peso = st.number_input("Peso actual (kg)", format="%.2f")
    
    if st.button("Guardar Registro"):
        nuevo_registro = pd.DataFrame([[fecha, jugador, peso]], columns=['Fecha', 'Jugador', 'Peso'])
        st.session_state.datos = pd.concat([st.session_state.datos, nuevo_registro]).drop_duplicates()
        st.success("¡Registrado!")

# --- CÁLCULO DE PUNTOS ---
# Aquí iría la lógica que compara el peso de la semana actual vs la anterior
# y otorga 1 punto al que tenga la diferencia negativa más grande.

# --- VISUALIZACIÓN ---
col1, col2 = st.columns(2)

with col1:
    st.write("### Evolución del Peso")
    if not st.session_state.datos.empty:
        fig = px.line(st.session_state.datos, x="Fecha", y="Peso", color="Jugador", markers=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Aún no hay datos registrados.")

with col2:
    st.write("### Marcador de Puntos")
    # Tabla resumen de puntos
    puntuacion = {"Jugador 1": 0, "Jugador 2": 0}
    st.table(pd.DataFrame.from_dict(puntuacion, orient='index', columns=['Puntos']))

st.divider()
st.info("Nota: El reto finaliza el 4 de mayo. ¡Dale con todo!
