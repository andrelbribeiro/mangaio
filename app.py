import streamlit as st
from sidebar_components.matematica import sidebar_matematica
from sidebar_components.geografia import sidebar_geografia
from sidebar_components.historia import sidebar_historia2
from sidebar_components.historia import sidebar_historia_deflagracao_revolta_1824
from sidebar_components.historia import sidebar_historia_repressao_imperial
from sidebar_components.historia import sidebar_historia_consequencias
# from sidebar_components.Informacoes import sidebar_informacoes


st.set_page_config(page_title="MangaioEdu", layout="wide")

st.sidebar.title("📚 Mangaio - Uma Plataforma Educacional Colaborativa")

with st.sidebar.expander("História", expanded=False):
    st.markdown("### Subtemas")
    subtema_escolhido = st.radio("Escolha um subtema", [
        "Crise do Primeiro Reinado", "Insatisfação do Nordeste", "Influências Liberais e Republicanas",
        "Deflagração da Revolta (1824)", "Repressão Imperial", "Consequências"], key="subtema")
st.write("Subtema selecionado:", subtema_escolhido)

if subtema_escolhido == "Crise do Primeiro Reinado":
    sidebar_historia2()

if subtema_escolhido == "Deflagração da Revolta (1824)":
    sidebar_historia_deflagracao_revolta_1824()

if subtema_escolhido == "Repressão Imperial":
    sidebar_historia_repressao_imperial()

if subtema_escolhido == "Consequências":
    sidebar_historia_consequencias()

sidebar_geografia()

sidebar_matematica()

# topico_matematica = sidebar_matematica()

# st.write("Tópico de matemática: ", topico_matematica)

# sidebar_informacoes()
