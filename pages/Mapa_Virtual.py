import streamlit as st

# Título da página
st.title("Exemplo de Mapa AR com A-Frame no Streamlit")

# Adicionando conteúdo HTML com AR.js e A-Frame dentro do Streamlit
st.markdown(
    """
    <html>
    <head>
      <title>Mapa AR com A-Frame</title>
      <!-- Incluir A-Frame -->
      <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
      <!-- Incluir AR.js -->
      <script src="https://cdn.jsdelivr.net/gh/AR-js-org/AR.js/aframe/build/aframe-ar.js"></script>
    </head>
    <body style="margin: 0; overflow: hidden;">
      <!-- Definindo a cena AR -->
      <a-scene embedded arjs="sourceType: webcam; debugUIEnabled: false; trackingMethod: best;">
        <!-- Definir marcador AR para detectar o objeto -->
        <a-marker preset="hiro">
          <!-- Adicionar um mapa ou objeto 3D ao marcador -->
          <a-box position="0 0.5 0" material="color: #4CC3D9"></a-box>
        </a-marker>
        <!-- Adicionando a câmera AR -->
        <a-entity camera></a-entity>
      </a-scene>
    </body>
    </html>
    """, unsafe_allow_html=True
)

st.write("""
Neste exemplo, o conteúdo de realidade aumentada (AR) foi integrado ao Streamlit.
Você pode ver a cena AR ao apontar a câmera para o marcador 'hiro' (um marcador padrão do AR.js).
""")
