import  folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

idhm = pd.read_excel("./doc/idhm_dados.xlsx")

geojson_url = "https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-33-mun.json"

mapa_idhm_rj = folium.Map([-21.93009349109802, -42.60928289352865],
                          tiles = "cartodbpositron",
                          zoom_start = 8)
#Adiconando mapa coropletico
folium.Choropleth(geo_data = geojson_url,
                  data = idhm,
                  fill_color="OrRd",
                  columns = ["Cidade", "IDHM"],
                  key_on = "feature.properties.name").add_to(mapa_idhm_rj)


estilo = lambda x: {"fillColor":"white",
                    "color":"black",
                    "fillOpacity":0.001,
                    "weight": 1}

estilo_destaque = lambda x:{"fillColor":"darkBlue",
                            "color": "black",
                            "fillOpacity": 0.5,
                            "weight": 1}

highlight = folium.features.GeoJson(data=geojson_url,
                                    style_function = estilo,
                                    highlight_function = estilo_destaque) 

folium.features.GeoJsonTooltip(fields = ["name"],
                               aliases = ["Cidade"],
                               style = ("background-color:write")).add_to(highlight)


#Teste

# latitude = -21.93009349109802 # row['Latitude']  # Certifique-se de ter a coluna de latitude na planilha
# longitude = -42.60928289352865 # row['Longitude']  # Certifique-se de ter a coluna de longitude na planilha
# cidade = ['Cidade']

#     # URL do vídeo (Exemplo com YouTube)
# video_url = f"https://www.youtube.com/embed/dQw4w9WgXcQ"  # Substitua pelo vídeo desejado

#     # Criar o marcador com um ícone personalizado
# icon = folium.Icon(icon="cloud", icon_color="white", color="blue")  # Ícone do marcador
# marker = folium.Marker([latitude, longitude], icon=icon)

#     # Criar o popup com o vídeo
# popup_content = f"""
#     <h3>{cidade}</h3>
#     <iframe width="300" height="200" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
#     """
# marker.add_popup(popup_content)  # Adiciona o popup ao marcador

#     # Adicionar o marcador ao mapa
# marker.add_to(mapa_idhm_rj)


#FimTest

st.title("Mangaio - Uma plataforma educacional colaborativa")

mapa_idhm_rj.add_child(highlight)              

st_folium(mapa_idhm_rj, width=700)