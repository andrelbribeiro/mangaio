import streamlit as st
from streamlit_folium import st_folium
import folium

# Dados de exemplo: coordenadas e vídeos
points = [
    {"name": "Ponto 1", "coords": [-8.0476, -34.8770], "vídeo": "https://www.youtube.com/watch?v=bW_h4mNJs1Y"},
    #{"name": "Ponto 2", "coords": [-8.0526, -34.8805], "audio": "audio2.mp3"},
]

# Função para gerar URL de embed do YouTube
def get_youtube_embed_url(video_url):
    video_id = video_url.split("v=")[-1]
    return f"https://www.youtube.com/embed/{video_id}"

st.header("Mangaio - Uma plataforma educacional colaborativa")

# Configurar página do Streamlit
st.set_page_config(page_title="Mapa Interativo com Vídeos e Áudios", layout="wide")

# Criar mapa inicial
m = folium.Map(location=[-8.05, -34.88], zoom_start=14)

# Adicionar marcadores com vídeos e áudios
for point in points:
    popup_content = f"<b>{point['name']}</b><br>"
    
    # Adicionar vídeo se disponível
    if "vídeo" in point:
        embed_url = get_youtube_embed_url(point["vídeo"])
        popup_content += f"""
        <iframe width="400" height="225" src="{embed_url}" frameborder="0" allowfullscreen></iframe>
        """
    
    # Adicionar áudio se disponível
    # if "audio" in point:
    #     popup_content += f"""
    #     <audio controls>
    #         <source src="{point['audio']}" type="audio/mpeg">
    #         Seu navegador não suporta o elemento de áudio.
    #     </audio>
    #     """

    # Criar o marcador
    folium.Marker(
        location=point["coords"],
        popup=popup_content,
    ).add_to(m)

# Exibir o mapa no Streamlit
st.write("### Mapa com Vídeos e Áudios")
st_map = st_folium(m, width=700, height=500)
