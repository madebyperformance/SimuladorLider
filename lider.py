import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#Importar logo
im = Image.open(r'logo.png')
im2 = Image.open(r'foguete.png')

# Define as cores da página
st.set_page_config(
    page_title='Simulador Partnership Líder',
    page_icon=im,
    layout='wide')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown('<div style="position: fixed; bottom: 0; right: 100px;"><p style="color: white;"><span style="color:black;font-size: 20px;font-family: Barlow Semibold;">MADE BY </span><span style="color:#9966FF;font-size: 20px; font-family: Barlow Semibold, sans-serif;">PERFORMANCE</span></p></div>', unsafe_allow_html=True)

def link():
    st.sidebar.markdown("<a href='https://madebyperformance-simulador-g10s10-simuladorg10s10-83xtig.streamlit.app/' target='_blank' style='text-decoration: none; font-family: Barlow; font-weight: bold; font-size: 22px; color: white;'>SIMULADOR G10 E S10</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<span style='font-family: Barlow; color: white; font-size: 14px;'>Clique acima para ser redirecionado ao Simulador do G10 e S10 2023.</span>", unsafe_allow_html=True)

link()

st.title('Simulador Partnership Líder - 2024')
st.caption("Use este simulador para calcular quanto de premiação você poderá receber ao final do ano. Importante frisar que a premiação é calculada em cima de valores preenchidos por você, devem ser considerados como uma aproximação.")

#fat meta
fat_m =st.number_input("Objetivo de Faturamento mínimo",format="%.0f")
fat_med = (fat_m * 1.08974358974359)
fat_max = ( fat_m * 1.34615384615385)
fat_m2="{:,.0f}".format(fat_m)
fat_m3="{:,.0f}".format(fat_med) 
fat_m4="{:,.0f}".format(fat_max) 

fat_m2 = fat_m2.replace(",",".")
fat_m3 = fat_m3.replace(",",".")
fat_m4 = fat_m4.replace(",",".")

st.caption(f"Objetivo Faturamento Mínimo: R$ {fat_m2}")
st.caption(f"Objetivo Faturamento Médio: R$ {fat_m3}")
st.caption(f"Objetivo Faturamento Máximo: R$ {fat_m4}")

#fat feito
fat=st.number_input("Faturamento Mês",format="%.0f")
fat2="{:,.0f}".format(fat) 
fat2 = fat2.replace(",",".")
st.caption(f"Faturamento total Selecionada: R$ {fat2}")

#incremento
inc=st.number_input("Incremento Mês",format="%.0f")
inc2="{:,.0f}".format(inc) 
inc2 = inc2.replace(",",".")
st.caption(f"Incremento total Selecionada: R$ {inc2}")

#NPS
nps=st.number_input("NPS Aniversário dos últimos 6 meses:")

#Calculando premiação
if st.button("Calcular Premiação"):

    #premiação Fat:
    if fat >= fat_max:
        fatp = (fat/1000000)*40000
        incp = 0
    elif fat >= fat_med and fat < fat_max:
        fatp = (fat/1000000)*30000
        incp = 0
    elif fat >= fat_m and fat < fat_med:
        fatp = (fat/1000000)*20000
        incp = 0
    elif fat > fat_m:
        fatp = 0
        #premiação incremento:
        if inc >= 5000000:
            incp = (inc/1000000)*500
        elif inc >= 3000000 and inc < 5000000:
            incp = (inc/1000000)*375
        elif inc >= 2000000 and inc < 3000000:
            incp = (inc/1000000)*250
        elif inc >= 1000000 and inc < 2000000:
            incp = (inc/1000000)*125
        elif inc > 2000000:
            incp = 0
            
    premf = (fatp+incp)

    premf="{:,.0f}".format(premf) 
    premf = premf.replace(",",".")
    
    incp="{:,.0f}".format(incp) 
    incp = incp.replace(",",".")
    
    fatp="{:,.0f}".format(fatp) 
    fatp = fatp.replace(",",".")
        
    valores = [["Premiação Faturamento",fatp],["Premiação Incremento",incp],["Premiação Final",premf]]
    df = pd.DataFrame(valores,columns=['KPI','R$ em Opções de Ações'])

    st.dataframe(df) 
