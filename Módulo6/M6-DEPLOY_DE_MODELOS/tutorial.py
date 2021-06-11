import streamlit as st

import streamlit as st

# Text/Title
st.title("Este é o title do streamlit")

# Header/Subheader - como em HTML
st.header("Header do streamlit")
st.subheader("Subheader do streamlit")

# Texto simples
st.text("Hello World - text")

# Markdown - como no Jupyter
st.markdown("#### Markdown - como no Jupyter")

st.success("Sucesso!")

st.info("Informações!")

st.warning("Isto é um aviso")

st.error("Isto é um aviso - Danger")

st.exception("NomeErro('name three not defined')")

# Chamar o Help
st.help(range)

# Checkbox - o que aparecerá abaixo é condicional
if st.checkbox("Mostrar/Esconder"):
	st.text("Apresentar ou esconder o Widget")

# Radio Buttons
status = st.radio("Qual é seu status?",("Ativo","Inativo"))

if status == 'Ativo':
	st.success("Você está Ativo")
    
else:
	st.warning("Você está inativo, volte à ativa!")

# SelectBox
occupation = st.selectbox("Sua Ocupação",["Programador","Data Scientist","Professor","Executivo"])
st.write("Você escolheu a opção ",occupation)

# MultiSelect
location = st.multiselect("Onde você mora",("Centro","Zona Sul","Zona Norte","Zona Leste","Zona Oeste"))
st.write("Você selecionou",len(location),"locais")

# Slider
level = st.slider("Qual sua avaliação do produto?",1,5)

# Buttons
st.button("Botão simples")

if st.button("Apertar"):
	st.text("Thank you, come again")

# Capturar input do usuário
firstname = st.text_input("Nos diga seu nome, por favor","Digite aqui..")
if st.button("Submit"):
	result = firstname.title()
	st.success(result + "!!!")

# Text Area
message = st.text_area("Nos dê seu feedback","Digite aqui..")
if st.button("Submeter"):
	result = message.title()
	st.success(result)

# Input Data
import datetime
today = st.date_input("Data da consulta",datetime.datetime.now())

# Input Time
the_time = st.time_input("Horário da consulta",datetime.time())

# Imagens
from PIL import Image
img = Image.open("asdf.png")
st.image(img,width=300,caption="6+3+3")

# Videos
vid_file = open("Genius S01E01 Einstein Chapter One.mp4","rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

# Audio
audio_file = open("AC DC - Jail break.mp3","rb").read()
st.audio(audio_file,format='audio/mp3')

# Write - utilização de funções
st.write("Texto")
texto  = "texto teste"
st.write(texto.upper())

# Para mostrar código Python
st.text("Mostra código formatado")
st.code("import numpy as np")

# Displaying JSON - Formatado
st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(50):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting .."):
     time.sleep(10)
     st.success("Finished!")


# SIDEBARS
st.sidebar.header("Sobre")
st.sidebar.text("Menu")
