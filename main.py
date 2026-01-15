import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Reto de Peso 2026", layout="wide")

st.title("🏆 Reto de Peso: 18 Feb - 4 May")

# Conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Leer datos existentes
df = conn.read(ttl="0") # ttl="0" para que refresque al instante

# Formulario de entrada
with st.sidebar:
    st.header("Registrar Peso")
    with st.form(key="peso_form"):
        fecha = st.date_input("Fecha del lunes")
        jugador = st.selectbox("Jugador", ["Jugador 1", "Jugador 2"])
        peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
        submit_button = st.form_submit_button(label="Guardar Peso")

    if submit_button:
        nuevo_dato = pd.DataFrame([{"Fecha": str(fecha), "Jugador": jugador, "Peso": peso}])
        df = pd.concat([df, nuevo_dato], ignore_index=True)
        conn.update(data=df)
        st.success("¡Peso guardado correctamente!")
        st.rerun()

# Mostrar Gráfica
if not df.empty:
    st.subheader("Evolución Semanal")
    st.line_chart(df, x="Fecha", y="Peso", color="Jugador")
else:
    st.info("Aún no hay datos. Registra tu primer peso en el menú lateral.")

