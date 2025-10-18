import streamlit as st
import folium
from streamlit.components.v1 import html

# Configuración de la app
st.set_page_config(
    layout="wide",
    page_title="Geocaching Talamanca",
    initial_sidebar_state="collapsed"  # Colapsar sidebar en móviles
)

st.title("Geocaching en Talamanca de Jarama")

# Crear mapa centrado en Talamanca de Jarama con las nuevas coordenadas
m = folium.Map(
    location=[40.750, -3.515], 
    zoom_start=15,
    control_scale=True,
    prefer_canvas=True  # Mejor rendimiento en móviles
)

# Añadir plugin para hacer el mapa responsive
m.add_child(folium.plugins.Responive())

# Link único del Google Form
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSdMk3kx-qkhmXvhBpI0m0Fo-EImLBDChoFP5oXf3gq4JokdnQ/viewform?usp=dialog"

# URL base para las imágenes en GitHub (usando raw.githubusercontent.com para acceso directo)
github_image_base = "https://raw.githubusercontent.com/forest-scanner/geocatching_talamanca/main/"

# Lista de tesoros con coordenadas actualizadas
tesoros = [
    {
        "nombre": "Puente de Madera",
        "lat": 40.75454145141272, 
        "lon": -3.5166748600339512,
        "pista": "<h4>En el puente de madera sobre el cauce de riego del río Jarama, busca en las oquedades de un árbol cercano al río.</h4>",
        "imagen": "lugar1.jpg"
    },
    {
        "nombre": "Puente Romano", 
        "lat": 40.750975092294915, 
        "lon": -3.5197053896261923,
        "pista": "<h4>En el antiguo puente romano, busca los lugares donde se pagaba el peaje en la antigüedad.</h4>",
        "imagen": "lugar2.jpg"
    },
    {
        "nombre": "El Ancla",
        "lat": 40.7491635912311, 
        "lon": -3.516954501691597,
        "pista": "<h4>De hierro nací, mas tengo alma de espera, amé un azul que ya no me espera. Sin agua respiro, sin olas suspiro, atada a la tierra, sueño mi retiro. ¿Qué soy, que sin rumbo ni amar, muero quieta, queriendo anclar?</h4>",
        "imagen": "lugar3.jpg"
    },
    {
        "nombre": "Bosque de Olivos",
        "lat": 40.746844291501326, 
        "lon": -3.5147752238552545,
        "pista": "<h4>Bosque de olivos centenarios frente a la Cartuja de Talamanca. La Cartuja es una finca del siglo XVI que conserva la memoria arquitectónica y cultural de los frailes cartujos del Monasterio de El Paular.</h4>",
        "imagen": "lugar4.jpg"
    },
    {
        "nombre": "Adivinanza 1",
        "lat": 40.74546455716086, 
        "lon": -3.5119383775703725,
        "pista": "<h4>Vuelo sin alas, corro sin pies, bajo por un cable, ¿sabes quién es? (Busca el juego infantil que se desliza por un cable)</h4>",
        "imagen": "lugar5.jpg"
    },
    {
        "nombre": "Adivinanza 2", 
        "lat": 40.74530341700391, 
        "lon": -3.5125995134186145,
        "pista": "<h4>En el centro del patio mi canto despierta, brota del mármol el agua que acierta. No tengo garganta, pero murmuro, soy vieja y clara, espejo seguro. (Busca la fuente antigua)</h4>",
        "imagen": "lugar6.jpg"
    },
    {
        "nombre": "Fragmento Histórico",
        "lat": 40.746441858564744, 
        "lon": -3.51212759972465,
        "pista": "<h4>Fragmento de piedra que guarda silencio, cicatriz del tiempo sobre la tierra. Fuiste muralla, guardiana de sueños, hoy sólo el viento te ronda y te nombra. (Busca los restos de la antigua muralla)</h4>",
        "imagen": "lugar7.jpg"
    },
    {
        "nombre": "Ermita de los Milagros",
        "lat": 40.745798790221286, 
        "lon": -3.513361041851946,
        "pista": "<h4>Pequeña y sola, guarda su canto, piedra que reza al paso del tiempo. Su ábside mira al valle en silencio, y en cada grieta duerme un milagro.</h4>",
        "imagen": "lugar8.jpg"
    }
]

# Agregar marcadores con popups de Folium que incluyen imágenes
for t in tesoros:
    gmaps_link = f"https://www.google.com/maps/dir/?api=1&destination={t['lat']},{t['lon']}"
    image_url = f"{github_image_base}{t['imagen']}"
    
    popup_html = f"""
    <div style="width: 350px; max-width: 90vw;">
        <b style="font-size: 16px;">{t['nombre']}</b><br><br>
        <div style="text-align: center; margin-bottom: 10px;">
            <img src="{image_url}" alt="{t['nombre']}" style="width: 100%; max-height: 200px; object-fit: cover; border-radius: 8px; border: 2px solid #ddd;">
        </div>
        {t['pista']}
        <div style="margin-top: 15px; text-align: center;">
            <a href='{gmaps_link}' target='_blank' style='background-color: #4CAF50; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px; display: inline-block; margin-right: 10px; margin-bottom: 5px;'>Ir aquí</a>
            <a href='{google_form_link}' target='_blank' style='background-color: #2196F3; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px; display: inline-block; margin-bottom: 5px;'>Marcar como encontrado</a>
        </div>
    </div>
    """
    
    # Color diferente para la Ermita para destacarla
    icon_color = "purple" if t["nombre"] == "Ermita de los Milagros" else "red"
    
    folium.Marker(
        location=[t["lat"], t["lon"]],
        popup=folium.Popup(popup_html, max_width=400),
        icon=folium.Icon(color=icon_color, icon="flag", prefix="fa")
    ).add_to(m)

# CSS personalizado para hacer el mapa responsive
responsive_css = """
<style>
/* Hacer que el mapa ocupe toda la pantalla en móviles */
@media (max-width: 768px) {
    .main .block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Asegurar que el iframe del mapa ocupe toda la pantalla */
    iframe {
        height: 80vh !important;
        min-height: 500px;
    }
}

/* Mejorar la visualización en pantallas pequeñas */
@media (max-width: 480px) {
    iframe {
        height: 75vh !important;
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
}
</style>
"""

# Aplicar CSS
st.markdown(responsive_css, unsafe_allow_html=True)

# Convertir mapa a HTML para mostrar en Streamlit
map_html = m._repr_html_()

# Envolver el mapa en un contenedor responsive
responsive_map_html = f"""
<div class="map-container">
{map_html}
</div>
"""

# Mostrar el mapa con configuración responsive
html(responsive_map_html, height=600, scrolling=True)

# Información adicional en un expander para ahorrar espacio en móviles
with st.sidebar:
    with st.expander("🗺️ Instrucciones del Geocaching", expanded=False):
        st.markdown("""
        1. **Haz clic en cualquier marcador** para ver la pista y una imagen del lugar
        2. **Usa el botón 'Ir aquí'** para abrir Google Maps 
        3. **Busca el tesoro** en la ubicación indicada
        4. **Marca como encontrado** cuando lo encuentres

        **Recuerda:** Los tesoros pueden ser pequeños objetos o códigos QR.
        """)
    
    with st.expander("📍 Tesoros Disponibles", expanded=False):
        st.markdown("""
        - Puente de Madera
        - Puente Romano  
        - El Ancla
        - Bosque de Olivos
        - Adivinanza 1 (juego infantil)
        - Adivinanza 2 (fuente)
        - Fragmento Histórico (muralla)
        - **Ermita de los Milagros** ✨
        """)
    
    with st.expander("📝 Formulario", expanded=False):
        st.markdown(f"""
        Usa el mismo formulario para marcar cualquier tesoro como encontrado.
        
        [Acceder al formulario]({google_form_link})
        """)

# Añadir un pequeño footer
st.sidebar.markdown("---")
st.sidebar.markdown("*Geocaching Talamanca de Jarama - ¡Disfruta explorando!*")


