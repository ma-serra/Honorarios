import streamlit as st
import re
from num2words import num2words

# Configurações da página inicial
def pagina_inicial():
    st.set_page_config(page_icon="calculadora_svg.svg", page_title="Calculadora de Honorários Adv!")
    st.image("calculadora_svg.svg", width=50)
    st.title('Calculadora de Honorários Advocatícios!', anchor=False)

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

# Converte o valor para texto por extenso em português
def valor_por_extenso(valor):
    return num2words(valor, lang='pt_BR', to='currency')