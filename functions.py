import streamlit as st
import re

# Função para validar o número do processo
def validar_processo(numero):
    pattern = r'^\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}$'
    return re.match(pattern, numero) is not None

# Função para calcular o valor do Honorário
def calcular_honorario(valor_total, porcentagem):
    return valor_total * (porcentagem / 100)

# Função formatar valor com duas casas decimais e separador de milhar
def formatar_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    return "R$ " + valor_formatado.replace(',', 'X').replace('.', ',').replace('X', '.')

# Cria sidebar
def sidebar():
    st.sidebar.title('Informações')
    st.sidebar.markdown(f"""Desenvolvido por **PdeNM9**. Contribua para o projeto pela chave PIX: pdenm9@gmail.com""")
