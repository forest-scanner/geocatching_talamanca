import streamlit as st
import folium
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

/* Botón de ubicación fijo */
.location-button {
    position: absolute !important;
    top: 10px !important;
    right: 10px !important;
    z-index: 1000 !important;
    padding: 12px 15px !important;
    background-color: #28a745 !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    cursor: pointer !important;
    font-size: 14px !important;
    font-weight: bold !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
}
</style>
"""

# Aplicar CSS
st.markdown(responsive_css, unsafe_allow_html=True)

# Convertir mapa a HTML para mostrar en Streamlit
map_html = m._repr_html_()

# Script JavaScript simplificado y mejorado
gps_script = """
<script>
// Función para obtener la ubicación
function getLocation() {
    if (navigator.geolocation) {
        // Cambiar texto del botón
        var button = document.getElementById('gps-button');
        if (button) {
            button.innerHTML = '🔄 Buscando...';
            button.disabled = true;
        }
        
        // Obtener ubicación
        navigator.geolocation.getCurrentPosition(
            function(position) {
                showPosition(position);
                // Restaurar botón
                if (button) {
                    button.innerHTML = '📍 Mi Ubicación';
                    button.disabled = false;
                }
            },
            function(error) {
                handleLocationError(error);
                // Restaurar botón
                if (button) {
                    button.innerHTML = '📍 Mi Ubicación';
                    button.disabled = false;
                }
            },
            {
                enableHighAccuracy: true,
                timeout: 15000,
                maximumAge: 60000
            }
        );
    } else {
        alert("Tu navegador no soporta geolocalización.");
    }
}

// Mostrar posición en el mapa
function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    
    // Buscar el mapa de Leaflet
    var mapElements = document.getElementsByClassName('folium-map');
    if (mapElements.length === 0) {
        alert("No se pudo encontrar el mapa. Recarga la página.");
        return;
    }
    
    var map = mapElements[0]._leaflet_map;
    
    // Eliminar marcador anterior si existe
    if (window.currentLocationMarker) {
        map.removeLayer(window.currentLocationMarker);
    }
    
    // Crear icono personalizado
    var greenIcon = L.divIcon({
        html: '<div style="background-color: green; width: 20px; height: 20px; border-radius: 50%; border: 3px solid white; box-shadow: 0 0 5px rgba(0,0,0,0.5);"></div>',
        iconSize: [20, 20],
        className: 'current-location-marker'
    });
    
    // Añadir marcador
    window.currentLocationMarker = L.marker([lat, lon], {icon: greenIcon}).addTo(map);
    
    // Añadir círculo de precisión
    var accuracy = position.coords.accuracy;
    L.circle([lat, lon], {
        color: 'green',
        fillColor: '#30c230',
        fillOpacity: 0.2,
        radius: accuracy
    }).addTo(map);
    
    // Centrar mapa en la ubicación
    map.setView([lat, lon], 16);
    
    // Mostrar popup
    window.currentLocationMarker.bindPopup(
        '<b>¡Estás aquí!</b><br>' +
        'Lat: ' + lat.toFixed(6) + '<br>' +
        'Lon: ' + lon.toFixed(6)
    ).openPopup();
    
    console.log("Ubicación encontrada: " + lat + ", " + lon);
}

// Manejar errores
function handleLocationError(error) {
    var message;
    switch(error.code) {
        case error.PERMISSION_DENIED:
            message = "Permiso de ubicación denegado. Por favor, permite el acceso a tu ubicación en la configuración del navegador.";
            break;
        case error.POSITION_UNAVAILABLE:
            message = "Información de ubicación no disponible.";
            break;
        case error.TIMEOUT:
            message = "Tiempo de espera agotado al buscar la ubicación.";
            break;
        default:
            message = "Error desconocido al obtener la ubicación.";
    }
    alert("Error: " + message);
}

// Añadir botón al mapa
function addLocationButton() {
    // Esperar a que el mapa se cargue
    setTimeout(function() {
        var mapContainer = document.querySelector('.folium-map');
        if (mapContainer) {
            // Crear botón
            var button = document.createElement('button');
            button.id = 'gps-button';
            button.className = 'location-button';
            button.innerHTML = '📍 Mi Ubicación';
            button.onclick = getLocation;
            
            // Añadir botón al mapa
            mapContainer.appendChild(button);
            console.log("Botón de ubicación añadido");
        } else {
            // Reintentar si no se encuentra el mapa
            setTimeout(addLocationButton, 500);
        }
    }, 1000);
}

// Iniciar cuando se carga la página
document.addEventListener('DOMContentLoaded', addLocationButton);
</script>
"""

# Combinar mapa HTML con el script
full_map_html = f"""
<div class="map-container">
{map_html}
</div>
{gps_script}
"""

# Mostrar el mapa
html(full_map_html, height=700, scrolling=False)

# Botón alternativo en Streamlit por si falla el JavaScript
st.sidebar.markdown("### 📍 Alternativa para GPS")
st.sidebar.markdown("""
Si el botón de ubicación en el mapa no funciona, puedes:

1. **Abrir Google Maps** para ver tu ubicación actual
2. **Comparar manualmente** con los marcadores del mapa
3. **Usar una app de mapas** externa para navegación

**Solución de problemas:**
- Asegúrate de que tu GPS esté activado
- Verifica los permisos de ubicación en tu navegador
- Intenta en un área con mejor señal
""")

# Información adicional en el sidebar
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
        - **Puente de Madera** - Río Jarama
        - **Puente Romano** - Peaje histórico  
        - **El Ancla** - Adivinanza
        - **Bosque de Olivos** - Cartuja
        - **Adivinanza 1** - Juego infantil
        - **Adivinanza 2** - Fuente antigua
        - **Fragmento Histórico** - Muralla
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








