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
st.markdown('<div style="position: fixed; bottom: 0; right: 1420px;"><p style="color: grey; font-size: 14px;font-family: Barlow;">Criado por Pedro Dantas</p></div>', unsafe_allow_html=True)

def link():
    st.sidebar.markdown("<a href='https://madebyperformance-simulador-g10s10-simuladorg10s10-83xtig.streamlit.app/' target='_blank' style='text-decoration: none; font-family: Barlow; font-weight: bold; font-size: 22px; color: white;'>SIMULADOR G10 E S10</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<span style='font-family: Barlow; color: white; font-size: 14px;'>Clique acima para ser redirecionado ao Simulador do G10 e S10.</span>", unsafe_allow_html=True)

link()

st.title('Simulador Partnership Líder')
st.caption("Use este simulador para calcular quanto de premiação você poderá receber ao final do ano. Importante frisar que a premiação é calculada em cima de valores preenchidos por você, devem ser considerados como uma aproximação.")

aai=st.number_input("Quanto Assessores premiados?",format="%.0f")

inc=st.number_input("Incremento total do ano da Filial",format="%.0f")
inc2="{:,.0f}".format(inc) 
inc2 = inc2.replace(",",".")
st.caption(f"Incremento total Selecionada: R$ {inc2}")

fat=st.number_input("Faturamento total do ano da Filial",format="%.0f")
fat2="{:,.0f}".format(fat) 
fat2 = fat2.replace(",",".")
st.caption(f"Faturamento total Selecionada: R$ {fat2}")

input_ROA=st.number_input("ROA médio do ano da Filial")
Expan=st.number_input("Expansão total da Filial",format="%.0f")

if st.button("Calcular Premiação"):

    #Calculando premiação
    if aai< 3:

        tx = 0
        if inc >= 300000000:
            incp = 60000
        elif inc >= 200000000 and inc < 300000000:
            incp = 40000
        elif inc >= 100000000 and inc < 200000000:
            incp = 20000
        elif inc < 100000000:
            incp = 0    
            
        if fat >= 4000000:
            fatp = 80000
        elif fat >= 3000000 and fat < 4000000:
            fatp = 60000
        elif fat >= 2000000 and fat < 3000000:
            fatp = 40000
        elif fat < 2000000:
            fatp = 0    

        premf = (fatp+incp)

        premf="{:,.0f}".format(premf) 
        premf = premf.replace(",",".")
        
        incp="{:,.0f}".format(incp) 
        incp = incp.replace(",",".")
        
        fatp="{:,.0f}".format(fatp) 
        fatp = fatp.replace(",",".")

        prems = 0
        tx = 0
        
        prems="{:,.0f}".format(prems) 
        prems = prems.replace(",",".")

        tx="{:.0%}".format(tx) 
            
        valores = [["Premiação Faturamento",fatp],["Premiação Incremento",incp],["% de Premiação do AAI",tx],["Premiação EquityBack",prems],["Premiação Final",premf]]
        df = pd.DataFrame(valores,columns=['KPI','R$ em Ações'])

        st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
        st.dataframe(df) 

    elif aai>=3:

        if aai >= 9:
            tx = 0.5
        elif aai >= 5 and aai < 9:
            tx = 0.25
        elif aai >= 3 and aai < 5:
            tx = 0.10
        elif aai < 3:
            tx = 0    

        if inc >= 300000000:
            incp = 0.2
            incp2 = 60000
        elif inc >= 200000000 and inc < 300000000:
            incp = 0.1
            incp2 = 40000
        elif inc >= 100000000 and inc < 200000000:
            incp = 0.05
            incp2 = 20000
        elif inc < 100000000:
            incp = 0    
            incp2 = 0
            
        if fat >= 4000000:
            fatp = 0.3
            fatp2 = 80000
        elif fat >= 3000000 and fat < 4000000:
            fatp = 0.2
            fatp2 = 60000
        elif fat >= 2000000 and fat < 3000000:
            fatp = 0.1
            fatp2 = 40000
        elif fat < 2000000:
            fatp = 0    
            fatp2 = 0
            
        prem = ((inc/1000000)*600)+((fat/1000000)*20000)
        #Faturamento final que será visto
        prems = (prem*tx)

        fatp = prems*fatp
        incp = prems*incp
        
        if fatp >= fatp2:
            fatp = fatp
        elif fatp < fatp2:
            fatp = fatp2
       
        if incp >= incp2:
            incp = incp
        elif incp < incp2:
            incp = incp2
            
        kpi1 = 0
        kpi2 = (prems*0.25)
        kpi3 = (prems*0.75)
        kpi4 = (prems*1)

        #Variante do ROA
        if input_ROA >= 0.75:
            pcroa = (prems*1)
        elif input_ROA >= 0.60 and input_ROA < 0.75:
            pcroa = (prems*0.75)
        elif input_ROA >= 0.30 and input_ROA < 0.60:
            pcroa = (prems*0.25)
        elif input_ROA < 0.30:
            pcroa = (prems*0)
            
        #Variante da Expansao
        if Expan >= 30:
            pcexp = 50000
        elif Expan >= 20 and Expan < 30:
            pcexp = 25000
        elif Expan >= 10 and Expan < 20:
            pcexp = 10000
        elif Expan < 10:
            pcexp = 0


        premf = (incp)+(fatp)+prems+pcroa+pcexp
        premf2 = (incp)+(fatp)+prems+pcroa+kpi2+pcexp
        premf3 = (incp)+(fatp)+prems+pcroa+kpi3+pcexp
        premf4 = (incp)+(fatp)+prems+pcroa+kpi4+pcexp
        
        #Ajustar formatação
        premf="{:,.0f}".format(premf) 
        premf = premf.replace(",",".")

        premf2="{:,.0f}".format(premf2) 
        premf2 = premf2.replace(",",".")

        premf3="{:,.0f}".format(premf3) 
        premf3 = premf3.replace(",",".")

        premf4="{:,.0f}".format(premf4) 
        premf4 = premf4.replace(",",".")

        kpi1="{:,.0f}".format(kpi1) 
        kpi1 = kpi1.replace(",",".")

        kpi2="{:,.0f}".format(kpi2) 
        kpi2 = kpi2.replace(",",".")

        kpi3="{:,.0f}".format(kpi3) 
        kpi3 = kpi3.replace(",",".")

        kpi4="{:,.0f}".format(kpi4) 
        kpi4 = kpi4.replace(",",".")


        incp="{:,.0f}".format(incp) 
        incp = incp.replace(",",".")
        
        fatp="{:,.0f}".format(fatp) 
        fatp = fatp.replace(",",".")

        prems="{:,.0f}".format(prems) 
        prems = prems.replace(",",".")

        pcroa="{:,.0f}".format(pcroa) 
        pcroa = pcroa.replace(",",".")
        
        pcexp="{:,.0f}".format(pcexp) 
        pcexp = pcexp.replace(",",".")

        tx="{:.0%}".format(tx) 

        #Tabela    
        valores = [["Premiação Faturamento",fatp,fatp,fatp,fatp],["Premiação Incremento",incp,incp,incp,incp],["% de Premiação do AAI",tx,tx,tx,tx],["Premiação EquityBack",prems,prems,prems,prems],["Adicional ROA",pcroa,pcroa,pcroa,pcroa],["Adicional Expansão",pcexp,pcexp,pcexp,pcexp],["Adicional KPI Global",kpi1,kpi2,kpi3,kpi4],["Premiação Final",premf,premf2,premf3,premf4]]
        df = pd.DataFrame(valores,columns=['KPI','Meta Global <80%','Meta Global >80%','Meta Global >90%','Meta Global >100%'])

        st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
        st.dataframe(df) 

    
