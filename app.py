import streamlit as st
import folium
from folium.plugins import LocateControl
from streamlit.components.v1 import html

# Configuración de la app
st.set_page_config(
    layout="wide",
    page_title="Geocaching Talamanca",
    initial_sidebar_state="collapsed"
)

st.title("Geocaching en Talamanca de Jarama")

# Crear mapa centrado en Talamanca de Jarama
m = folium.Map(
    location=[40.750, -3.515], 
    zoom_start=15,
    control_scale=True,
    tiles='OpenStreetMap'
)

# Añadir control de localización personalizado
LocateControl(
    auto_start=False,
    draw_circle=True,
    show_popup=True,
    strings={
        "title": "Mostrar mi ubicación",
        "popup": "¡Estás aquí!"
    }
).add_to(m)

# Link único del Google Form
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSdMk3kx-qkhmXvhBpI0m0Fo-EImLBDChoFP5oXf3gq4JokdnQ/viewform?usp=dialog"

# URL base para las imágenes en GitHub
github_image_base = "https://raw.githubusercontent.com/forest-scanner/geocatching_talamanca/main/"

# Lista de tesoros con coordenadas actualizadas
tesoros = [
    {
        "nombre": "Puente de Madera",
        "lat": 40.75454145141272, 
        "lon": -3.5166748600339512,
        "pista": "En el puente de madera sobre el cauce de riego del río Jarama, busca en las oquedades de un árbol cercano al río.",
        "imagen": "lugar1.jpg"
    },
    {
        "nombre": "Puente Romano", 
        "lat": 40.750975092294915, 
        "lon": -3.5197053896261923,
        "pista": "En el antiguo puente romano, busca los lugares donde se pagaba el peaje en la antigüedad.",
        "imagen": "lugar2.jpg"
    },
    {
        "nombre": "El Ancla",
        "lat": 40.7491635912311, 
        "lon": -3.516954501691597,
        "pista": "De hierro nací, mas tengo alma de espera, amé un azul que ya no me espera. Sin agua respiro, sin olas suspiro, atada a la tierra, sueño mi retiro. ¿Qué soy, que sin rumbo ni amar, muero quieta, queriendo anclar?",
        "imagen": "lugar3.jpg"
    },
    {
        "nombre": "Bosque de Olivos",
        "lat": 40.746844291501326, 
        "lon": -3.5147752238552545,
        "pista": "Bosque de olivos centenarios frente a la Cartuja de Talamanca. La Cartuja es una finca del siglo XVI que conserva la memoria arquitectónica y cultural de los frailes cartujos del Monasterio de El Paular.",
        "imagen": "lugar4.jpg"
    },
    {
        "nombre": "Adivinanza 1",
        "lat": 40.74546455716086, 
        "lon": -3.5119383775703725,
        "pista": "Vuelo sin alas, corro sin pies, bajo por un cable, ¿sabes quién es? (Busca el juego infantil que se desliza por un cable)",
        "imagen": "lugar5.jpg"
    },
    {
        "nombre": "Adivinanza 2", 
        "lat": 40.74530341700391, 
        "lon": -3.5125995134186145,
        "pista": "En el centro del patio mi canto despierta, brota del mármol el agua que acierta. No tengo garganta, pero murmuro, soy vieja y clara, espejo seguro. (Busca la fuente antigua)",
        "imagen": "lugar6.jpg"
    },
    {
        "nombre": "Fragmento Histórico",
        "lat": 40.746441858564744, 
        "lon": -3.51212759972465,
        "pista": "Fragmento de piedra que guarda silencio, cicatriz del tiempo sobre la tierra. Fuiste muralla, guardiana de sueños, hoy sólo el viento te ronda y te nombra. (Busca los restos de la antigua muralla)",
        "imagen": "lugar7.jpg"
    },
    {
        "nombre": "Ermita de los Milagros",
        "lat": 40.745798790221286, 
        "lon": -3.513361041851946,
        "pista": "Pequeña y sola, guarda su canto, piedra que reza al paso del tiempo. Su ábside mira al valle en silencio, y en cada grieta duerme un milagro.",
        "imagen": "lugar8.jpg"
    }
]

# Agregar marcadores con popups de Folium que incluyen imágenes
for t in tesoros:
    gmaps_link = f"https://www.google.com/maps/dir/?api=1&destination={t['lat']},{t['lon']}"
    image_url = f"{github_image_base}{t['imagen']}"
    
    # HTML mejorado para popups móviles
    popup_html = f"""
    <div style="width: 95vw; max-width: 400px; font-family: Arial, sans-serif;">
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px 8px 0 0; border-bottom: 2px solid #dee2e6;">
            <h3 style="margin: 0; color: #333; font-size: 18px; text-align: center;">{t['nombre']}</h3>
        </div>
        
        <div style="padding: 15px;">
            <div style="text-align: center; margin-bottom: 15px;">
                <img src="{image_url}" alt="{t['nombre']}" style="width: 100%; max-height: 180px; object-fit: cover; border-radius: 6px; border: 1px solid #ddd;">
            </div>
            
            <div style="background-color: #e9ecef; padding: 12px; border-radius: 6px; margin-bottom: 15px;">
                <p style="margin: 0; color: #495057; font-size: 16px; line-height: 1.4; text-align: left;">{t['pista']}</p>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <a href='{gmaps_link}' target='_blank' style='background-color: #28a745; color: white; padding: 12px; text-decoration: none; border-radius: 6px; text-align: center; font-size: 16px; font-weight: bold;'>
                    📍 Ir aquí con Google Maps
                </a>
                <a href='{google_form_link}' target='_blank' style='background-color: #007bff; color: white; padding: 12px; text-decoration: none; border-radius: 6px; text-align: center; font-size: 16px; font-weight: bold;'>
                    ✅ Marcar como encontrado
                </a>
            </div>
        </div>
    </div>
    """
    
    # Color diferente para la Ermita para destacarla
    icon_color = "purple" if t["nombre"] == "Ermita de los Milagros" else "red"
    
    folium.Marker(
        location=[t["lat"], t["lon"]],
        popup=folium.Popup(popup_html, max_width=500),
        icon=folium.Icon(color=icon_color, icon="flag", prefix="fa")
    ).add_to(m)

# CSS personalizado mejorado para móviles
responsive_css = """
<style>
/* Hacer que el mapa ocupe toda la pantalla en móviles */
@media (max-width: 768px) {
    .main .block-container {
        padding-top: 0.5rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        padding-bottom: 0.5rem;
    }
    
    /* Asegurar que el iframe del mapa ocupe toda la pantalla */
    iframe {
        height: 85vh !important;
        min-height: 450px;
    }
    
    /* Ajustar el título para móviles */
    h1 {
        font-size: 1.4rem !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
    }
    
    /* Mejorar los popups de Folium en móviles */
    .leaflet-popup-content {
        width: auto !important;
        margin: 10px !important;
    }
    
    .leaflet-popup-content-wrapper {
        border-radius: 10px !important;
        max-width: 95vw !important;
    }
}

/* Mejorar la visualización en pantallas muy pequeñas */
@media (max-width: 480px) {
    iframe {
        height: 80vh !important;
        min-height: 400px;
    }
    
    /* Ajustar el sidebar para móviles */
    section[data-testid="stSidebar"] {
        min-width: 100% !important;
        max-width: 100% !important;
    }
}

/* Asegurar que el mapa sea responsive */
.map-container {
    width: 100%;
    height: 100%;
    position: relative;
}

/* Mejorar la legibilidad general */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Botones más grandes para móviles */
@media (max-width: 768px) {
    .stButton button {
        width: 100%;
        margin-bottom: 8px;
        padding: 12px !important;
        font-size: 16px !important;
    }
}

/* Mejorar los enlaces en los popups para móviles */
.leaflet-popup-content a {
    font-size: 16px !important;
    padding: 12px !important;
    margin: 5px 0 !important;
}
</style>
"""

# Aplicar CSS
st.markdown(responsive_css, unsafe_allow_html=True)

# Convertir mapa a HTML para mostrar en Streamlit
map_html = m._repr_html_()

# Envolver el mapa en un contenedor
responsive_map_html = f"""
<div class="map-container">
{map_html}
</div>
"""

# Mostrar el mapa con configuración responsive
html(responsive_map_html, height=700)

# Información sobre la funcionalidad de ubicación
st.sidebar.markdown("### 📍 Mi Ubicación")
st.sidebar.markdown("""
**Cómo usar la ubicación:**

Haz clic en el botón de ubicación (el círculo con una flecha) en el mapa para:
- Activar la geolocalización
- Centrar el mapa en tu ubicación actual
- Ver un marcador con tu posición

**Si no funciona:**
- Asegúrate de tener el GPS activado
- Verifica los permisos de ubicación en tu navegador
- Comprueba que estás en un entorno HTTPS (necesario para geolocalización)
""")

# ... (el resto del sidebar)







