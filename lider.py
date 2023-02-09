import streamlit as st
import pandas as pd
import numpy as np

st.title('Simulador do Partnership 2023 - Líder')
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
        elif inc >= 200000000 and inc < 300000000:
            incp = 0.1
        elif inc >= 100000000 and inc < 200000000:
            incp = 0.05
        elif inc < 100000000:
            incp = 0    
            
        if fat >= 4000000:
            fatp = 0.3
        elif fat >= 3000000 and fat < 4000000:
            fatp = 0.2
        elif fat >= 2000000 and fat < 3000000:
            fatp = 0.1
        elif fat < 2000000:
            fatp = 0    

        prem = ((inc/1000000)*600)+((fat/1000000)*7500)
        #Faturamento final que será visto
        prems = (prem*tx)

        fatp = prems*fatp
        incp = prems*incp
     
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



        premf = (incp)+(fatp)+prems+pcroa
        premf2 = (incp)+(fatp)+prems+pcroa+kpi2
        premf3 = (incp)+(fatp)+prems+pcroa+kpi3
        premf4 = (incp)+(fatp)+prems+pcroa+kpi4
        
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

        tx="{:.0%}".format(tx) 

        #Tabela    
        valores = [["Premiação Faturamento",fatp,fatp,fatp,fatp],["Premiação Incremento",incp,incp,incp,incp],["% de Premiação do AAI",tx,tx,tx,tx],["Premiação EquityBack",prems,prems,prems,prems],["Adicional ROA",pcroa,pcroa,pcroa,pcroa],["Adicional KPI Global",kpi1,kpi2,kpi3,kpi4],["Premiação Final",premf,premf2,premf3,premf4]]
        df = pd.DataFrame(valores,columns=['KPI','Meta Global <80%','Meta Global >80%','Meta Global >90%','Meta Global >100%'])

        st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
        st.dataframe(df) 

    