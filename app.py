import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análisis interactivo de anuncios de autos usados')

# Cargar datos con control de errores
try:
    car_data = pd.read_csv('vehicles_us.csv')
    st.success('Datos cargados correctamente.')
except FileNotFoundError:
    st.error('No se encontró el archivo "vehicles_us.csv". Asegúrate de que esté en el mismo directorio.')
    st.stop()

# Descripción inicial
st.write("Usa los botones a continuación para generar visualizaciones interactivas de los datos.")

# Botón: Histograma del odómetro
if st.button('📊 Mostrar histograma del odómetro'):
    st.subheader('Distribución del kilometraje (odómetro)')
    fig = px.histogram(car_data, x='odometer', nbins=40, title='Histograma del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Espacio entre secciones
st.markdown('---')

# Botón: Gráfico de dispersión precio vs odómetro
if st.button('🔎 Mostrar dispersión Precio vs Odómetro'):
    st.subheader('Relación entre precio y kilometraje')
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Dispersión: Precio vs Odómetro',
        labels={'odometer': 'Kilometraje (odometer)', 'price': 'Precio (USD)'},
        opacity=0.6
    )
    st.plotly_chart(fig, use_container_width=True)
