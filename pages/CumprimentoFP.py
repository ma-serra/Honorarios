import streamlit as st

# 
st.write(
    """
    # Calculadora de Honorários Advocatícios!\n\n
    Cmprimento de Sentença contra a Fazenda Pública! 👋\n 
    ✨
    """
)

# Entrada de dados
processo = st.text_input('Insira o número do processo:', placeholder='Ex: 0123456-00.2099.8.05.0001')
exequente = st.text_input('Insira o nome do Exequente:', placeholder='Nome do exequente.')
executado = st.text_input('Insira o nome do Executado:', placeholder='Nome do executado.')
valor_homologado = st.number_input('Insira o valor homologado (R$):', placeholder='R$ 0,00')

porcentagem_sucumbencia = st.number_input('Insira a porcentagem dos honorários de sucumbência (%):', min_value=0)
porcentagem_contratual = st.number_input('Insira a porcentagem dos honorários contratuais (%):', min_value=0)
quantidade_advogados = st.number_input('Insira a quantidade de advogados', min_value=1)
