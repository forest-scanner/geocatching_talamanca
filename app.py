import streamlit as st
import folium
from streamlit.components.v1 import html

# Configuración de la app
st.set_page_config(layout="wide")
st.title("Geocaching en Talamanca de Jarama")

# Crear mapa centrado en Talamanca de Jarama
m = folium.Map(location=[40.748, -3.511], zoom_start=16)

# Link base del Google Form
google_form_link = "https://docs.google.com/forms/d/1IjqaIbFe7ZZWdIJ4acgxYhxWQtu5vC7kdmYYsgYcPNg/prefill"

# URL base para las imágenes en GitHub
github_image_base = "https://raw.githubusercontent.com/forest-scanner/geocatching_talamanca/main/"

# Lista de tesoros con pistas actualizadas e imágenes
tesoros = [
    {
        "nombre": "Puente de Madera",
        "lat": 40.7482, 
        "lon": -3.5105,
        "pista": "<h4>En el puente de madera sobre el cauce de riego del río Jarama, busca en las oquedades de un árbol cercano al río.</h4>",
        "imagen": "lugar1.JPG"
    },
    {
        "nombre": "Puente Romano", 
        "lat": 40.7486, 
        "lon": -3.5120,
        "pista": "<h4>En el antiguo puente romano, busca los lugares donde se pagaba el peaje en la antigüedad.</h4>",
        "imagen": "lugar2.JPG"
    },
    {
        "nombre": "Zona Deportiva",
        "lat": 40.7478, 
        "lon": -3.5112,
        "pista": "<h4>Lugar donde mayores y no tan mayores practican ejercicio estático: bicicletas y remo sin moverse del sitio.</h4>",
        "imagen": "lugar3.JPG"
    },
    {
        "nombre": "Bosque de Olivos",
        "lat": 40.7489, 
        "lon": -3.5098,
        "pista": "<h4>Bosque de olivos centenarios frente a la Cartuja de Talamanca. La Cartuja es una finca del siglo XVI que conserva la memoria arquitectónica y cultural de los frailes cartujos del Monasterio de El Paular.</h4>",
        "imagen": "lugar4.JPG"
    },
    {
        "nombre": "Adivinanza 1",
        "lat": 40.7475, 
        "lon": -3.5100,
        "pista": "<h4>Vuelo sin alas, corro sin pies, bajo por un cable, ¿sabes quién es? (Busca el juego infantil que se desliza por un cable)</h4>",
        "imagen": "lugar5.JPG"
    },
    {
        "nombre": "Adivinanza 2", 
        "lat": 40.7484, 
        "lon": -3.5115,
        "pista": "<h4>En el centro del patio mi canto despierta, brota del mármol el agua que acierta. No tengo garganta, pero murmuro, soy vieja y clara, espejo seguro. (Busca la fuente antigua)</h4>",
        "imagen": "lugar6.JPG"
    },
    {
        "nombre": "Fragmento Histórico",
        "lat": 40.7487, 
        "lon": -3.5122,
        "pista": "<h4>Fragmento de piedra que guarda silencio, cicatriz del tiempo sobre la tierra. Fuiste muralla, guardiana de sueños, hoy sólo el viento te ronda y te nombra. (Busca los restos de la antigua muralla)</h4>",
        "imagen": "lugar7.JPG"
    },
    {
        "nombre": "Ermita de los Milagros",
        "lat": 40.7492, 
        "lon": -3.5128,
        "pista": "<h4>Pequeña y sola, guarda su canto, piedra que reza al paso del tiempo. Su ábside mira al valle en silencio, y en cada grieta duerme un milagro.</h4>",
        "imagen": "lugar8.JPG"
    }
]

# Agregar marcadores con popups de Folium que incluyen imágenes
for t in tesoros:
    gmaps_link = f"https://www.google.com/maps/dir/?api=1&destination={t['lat']},{t['lon']}"
    form_link = f"{google_form_link}&entry.123456={t['nombre']}"  # Ajusta el entry.123456 según tu formulario
    image_url = f"{github_image_base}{t['imagen']}"
    
    popup_html = f"""
    <div style="width: 350px;">
        <b style="font-size: 16px;">{t['nombre']}</b><br><br>
        <div style="text-align: center; margin-bottom: 10px;">
            <img src="{image_url}" alt="{t['nombre']}" style="width: 100%; max-height: 200px; object-fit: cover; border-radius: 8px;">
        </div>
        {t['pista']}
        <div style="margin-top: 15px; text-align: center;">
            <a href='{gmaps_link}' target='_blank' style='background-color: #4CAF50; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px; display: inline-block; margin-right: 10px;'>Ir aquí</a>
            <a href='{form_link}' target='_blank' style='background-color: #2196F3; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px; display: inline-block;'>Marcar como encontrado</a>
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

# Convertir mapa a HTML para mostrar en Streamlit
map_html = m._repr_html_()
html(map_html, height=700)

# Información adicional
st.sidebar.markdown("### 🗺️ Instrucciones del Geocaching")
st.sidebar.markdown("""
1. **Haz clic en cualquier marcador** para ver la pista y una imagen del lugar
2. **Usa el botón 'Ir aquí'** para abrir Google Maps 
3. **Busca el tesoro** en la ubicación indicada
4. **Marca como encontrado** cuando lo encuentres

**Recuerda:** Los tesoros pueden ser pequeños objetos o códigos QR.

### 📍 Tesoros Disponibles
- Puente de Madera
- Puente Romano  
- Zona Deportiva
- Bosque de Olivos
- Adivinanza 1 (juego infantil)
- Adivinanza 2 (fuente)
- Fragmento Histórico (muralla)
- **Ermita de los Milagros** ✨

### 📸 ¡Novedad!
Ahora cada marcador incluye una foto del lugar para ayudarte en tu búsqueda.
""")

