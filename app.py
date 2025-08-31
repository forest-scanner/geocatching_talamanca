import streamlit as st
import folium
from streamlit.components.v1 import html

# Configuración de la app
st.set_page_config(layout="wide")
st.title("Geocaching en Talamanca de Jarama")

# Crear mapa centrado en Talamanca de Jarama
m = folium.Map(location=[40.748, -3.511], zoom_start=16)

# Link base del Google Form
google_form_link = "https://docs.google.com/forms/d/1IjqaIbFe7ZZWdIJ4acgxYhxWQtu5vC7kdmYYsgYcPNg/preview"

# Lista de tesoros con 10 pistas (letra más grande con <h4>)
tesoros = [
    {"nombre": "Pista 1", "lat": 40.7482, "lon": -3.5105,
     "pista": "<h4>El tiburón está en el agua, ¿verdad? Busca un puente de madera...</h4>"},
    {"nombre": "Pista 2", "lat": 40.7486, "lon": -3.5120,
     "pista": "<h4>Este secreto es muy antiguo... busca lo más antiguo de la zona verde, estará por debajo.</h4>"},
    {"nombre": "Pista 3", "lat": 40.7478, "lon": -3.5112,
     "pista": "<h4>Esto lo usan los mayores... ¿dónde van los mayores a hacer ejercicio?</h4>"},
    {"nombre": "Pista 4", "lat": 40.7489, "lon": -3.5098,
     "pista": "<h4>Busca un bosque de olivos frente a un edificio emblemático.</h4>"},
    {"nombre": "Pista 5", "lat": 40.7475, "lon": -3.5100,
     "pista": "<h4>Una pelota para lanzarte y avanzar muchos metros en pocos segundos...</h4>"},
    {"nombre": "Pista 6", "lat": 40.7484, "lon": -3.5115,
     "pista": "<h4>Esto dicen que da suerte si lo resuelves. Igual que algo que echa agua.</h4>"},
    {"nombre": "Pista 7", "lat": 40.7487, "lon": -3.5122,
     "pista": "<h4>Búsqueda de milagro: busca tu milagro monumental.</h4>"},
    {"nombre": "Pista 8", "lat": 40.7476, "lon": -3.5095,
     "pista": "<h4>Un lugar donde te harás soñar y ver las estrellas como está.</h4>"},
    {"nombre": "Pista 9", "lat": 40.7480, "lon": -3.5125,
     "pista": "<h4>Donde los romanos han estado, nosotros también estamos protegiéndonos.</h4>"},
    {"nombre": "Pista 10", "lat": 40.7479, "lon": -3.5090,
     "pista": "<h4>Lugar donde se hace deporte con amigos, encontrarás la pulsera de la amistad.</h4>"},
]

# Agregar marcadores con popups de Folium
for t in tesoros:
    gmaps_link = f"https://www.google.com/maps/dir/?api=1&destination={t['lat']},{t['lon']}"
    form_link = f"{google_form_link}?entry.123456={t['nombre']}"  # Reemplaza entry.123456 con tu campo real si quieres autocompletar
    popup_html = f"""
    <b>{t['nombre']}</b><br>
    {t['pista']}<br>
    <a href='{gmaps_link}' target='_blank'>Ir aquí</a><br>
    <a href='{form_link}' target='_blank'>Marcar como encontrado</a>
    """
    folium.Marker(
        location=[t["lat"], t["lon"]],
        popup=popup_html,
        icon=folium.Icon(color="blue", icon="star")
    ).add_to(m)

# Convertir mapa a HTML para mostrar en Streamlit
map_html = m._repr_html_()
html(map_html, height=700)
