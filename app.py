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
        height: 75vh !important;
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
        height: 70vh !important;
        min-height: 400px;
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

/* Estilo para el botón de ubicación */
.gps-button {
    background-color: #28a745 !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 12px 20px !important;
    font-size: 16px !important;
    font-weight: bold !important;
    cursor: pointer !important;
    margin-bottom: 10px !important;
    width: 100% !important;
}

.gps-button:disabled {
    background-color: #6c757d !important;
    cursor: not-allowed !important;
}
</style>
"""

# Aplicar CSS
st.markdown(responsive_css, unsafe_allow_html=True)

# Botón de GPS nativo de Streamlit
st.markdown("### 📍 Ubicación GPS")
gps_button = st.button(
    "📍 Activar GPS y Mostrar Mi Ubicación", 
    key="gps_button",
    use_container_width=True,
    type="primary"
)

# Convertir mapa a HTML
map_html = m._repr_html_()

# Script JavaScript mejorado para GPS
gps_script = """
<script>
// Variable global para el marcador
var currentLocationMarker = null;

// Función para obtener el mapa de Leaflet
function getLeafletMap() {
    // Buscar todos los elementos iframe que contengan mapas de Leaflet
    var iframes = document.getElementsByTagName('iframe');
    for (var i = 0; i < iframes.length; i++) {
        try {
            var iframe = iframes[i];
            // Verificar si este iframe contiene un mapa de Leaflet
            if (iframe.contentDocument && iframe.contentDocument.querySelector('.leaflet-container')) {
                var leafletContainer = iframe.contentDocument.querySelector('.leaflet-container');
                if (leafletContainer && leafletContainer._leaflet_map) {
                    return leafletContainer._leaflet_map;
                }
            }
        } catch (e) {
            // Ignorar errores de acceso entre iframes
            console.log("No se pudo acceder al iframe:", e);
        }
    }
    
    // Si no se encuentra en iframes, buscar directamente
    var leafletContainer = document.querySelector('.leaflet-container');
    if (leafletContainer && leafletContainer._leaflet_map) {
        return leafletContainer._leaflet_map;
    }
    
    return null;
}

// Función para obtener ubicación
function getCurrentLocation() {
    if (!navigator.geolocation) {
        alert("Tu navegador no soporta geolocalización.");
        return;
    }
    
    // Obtener el mapa
    var map = getLeafletMap();
    if (!map) {
        alert("Error: El mapa aún no está listo. Espera unos segundos y vuelve a intentarlo.");
        return;
    }
    
    // Mostrar mensaje de carga
    console.log("Buscando ubicación...");
    
    navigator.geolocation.getCurrentPosition(
        function(position) {
            showPosition(position, map);
        },
        function(error) {
            handleLocationError(error);
        },
        {
            enableHighAccuracy: true,
            timeout: 15000,
            maximumAge: 60000
        }
    );
}

// Mostrar posición en el mapa
function showPosition(position, map) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var accuracy = position.coords.accuracy;
    
    console.log("Ubicación encontrada:", lat, lon);
    
    // Eliminar marcador anterior si existe
    if (currentLocationMarker) {
        map.removeLayer(currentLocationMarker);
    }
    
    // Crear icono personalizado para ubicación actual
    var greenIcon = L.divIcon({
        html: '<div style="background-color: #28a745; width: 20px; height: 20px; border-radius: 50%; border: 3px solid white; box-shadow: 0 0 8px rgba(0,0,0,0.5);"></div>',
        iconSize: [25, 25],
        className: 'current-location-marker'
    });
    
    // Añadir marcador
    currentLocationMarker = L.marker([lat, lon], {icon: greenIcon}).addTo(map);
    
    // Añadir círculo de precisión
    L.circle([lat, lon], {
        color: '#28a745',
        fillColor: '#28a745',
        fillOpacity: 0.2,
        radius: accuracy
    }).addTo(map);
    
    // Centrar mapa en la ubicación
    map.setView([lat, lon], 16);
    
    // Añadir popup informativo
    currentLocationMarker.bindPopup(
        '<div style="text-align: center; min-width: 200px;">' +
        '<b>¡Estás aquí!</b><br>' +
        'Lat: ' + lat.toFixed(6) + '<br>' +
        'Lon: ' + lon.toFixed(6) + '<br>' +
        '<small>Precisión: ±' + Math.round(accuracy) + 'm</small>' +
        '</div>'
    ).openPopup();
    
    // Mostrar mensaje de éxito
    alert("¡Ubicación encontrada! Se ha añadido un marcador verde en tu posición.");
    
    // Mostrar coordenadas en la consola
    console.log("Tus coordenadas:", lat, lon);
}

// Manejar errores
function handleLocationError(error) {
    var message = "Error al obtener la ubicación: ";
    
    switch(error.code) {
        case error.PERMISSION_DENIED:
            message += "Has denegado el permiso de ubicación. Por favor, permite el acceso a tu ubicación en la configuración del navegador.";
            break;
        case error.POSITION_UNAVAILABLE:
            message += "La información de ubicación no está disponible. Verifica tu conexión y GPS.";
            break;
        case error.TIMEOUT:
            message += "El tiempo de espera se agotó. Intenta de nuevo.";
            break;
        default:
            message += "Error desconocido.";
    }
    
    alert(message);
    console.error("Error de geolocalización:", error);
}

// Función para inicializar cuando se presiona el botón
function initGPS() {
    console.log("Inicializando GPS...");
    
    // Esperar un momento para asegurar que el mapa esté cargado
    setTimeout(function() {
        getCurrentLocation();
    }, 500);
}

// Verificar si debemos ejecutar el GPS automáticamente
if (window.autoStartGPS) {
    initGPS();
    window.autoStartGPS = false;
}
</script>
"""

# Si se presionó el botón de GPS, activar el script
if gps_button:
    st.success("Buscando tu ubicación... Por favor, permite el acceso a tu ubicación cuando tu navegador lo solicite.")
    
    # Script para activar GPS cuando se carga la página
    activation_script = """
    <script>
    // Esperar a que la página esté completamente cargada
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            window.autoStartGPS = true;
        });
    } else {
        window.autoStartGPS = true;
    }
    </script>
    """
    
    # Combinar todo
    full_html = f"""
    <div class="map-container">
    {map_html}
    </div>
    {gps_script}
    {activation_script}
    """
else:
    # Solo mostrar mapa y script sin activación
    full_html = f"""
    <div class="map-container">
    {map_html}
    </div>
    {gps_script}
    """

# Mostrar el mapa
html(full_html, height=600)

# Información sobre GPS en el sidebar
st.sidebar.markdown("### 📍 Cómo usar el GPS")
st.sidebar.markdown("""
1. **Haz clic en el botón '📍 Activar GPS'** arriba del mapa
2. **Permite el acceso** a tu ubicación cuando el navegador lo solicite
3. **Espera** a que se procese tu ubicación
4. **Verás** un marcador verde en el mapa con tu posición

**Si ves el error 'mapa no está listo':**
- Espera 2-3 segundos después de que cargue el mapa
- Vuelve a hacer clic en el botón
- Recarga la página si es necesario

**Coordenadas:**
- Se mostrarán en un popup sobre el marcador verde
- También puedes verlas en la consola del navegador (F12)
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









