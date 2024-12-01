import streamlit as st

# Adiciona o título da página
st.title('WebAR com A-Frame')

# Usando a tag iframe para exibir conteúdo HTML (A-Frame) dentro do Streamlit
st.markdown(
    """
    <iframe 
        width="100%" 
        height="500px"
        src="https://aframe.io/aframe/examples/showcase/curved-mockups/" 
        frameborder="0">
    </iframe>
    """, 
    unsafe_allow_html=True
)

st.write("""
Este é um exemplo simples de como integrar **WebAR** usando o **A-Frame** dentro de uma aplicação Streamlit.
Você pode clicar e interagir com o conteúdo 3D diretamente na página.
""")
