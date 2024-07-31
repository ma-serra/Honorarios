import streamlit as st

import functions

from conceitos import get_conceito

# Cabeçalho de toda página do projeto
st.image("calculadora_svg.svg", width=50)

functions.sidebar()


# 
st.write(
    """
    # Calculadora de Honorários Advocatícios!\n\n
    Bem-vindo ao nosso glossário! 👋\n 
    Esta página mostra alguns conceitos úteis para entender os cálculos apresentados neste projeto ou por seu(sua) advogado(a).✨
    """
)

# Chama função que traz os conceitos
st.markdown(get_conceito())

# Rodapé
st.info(
    """
    Tem alguma crítica, sugestão ou ideia? 
    Encaminhe para o nosso e-mail: pdenm9@gmail.com
    """,
    icon="👾",
)

st.success(
    """
   Muito Obrigado por utilizar nosso site.
    """,
    icon="🗺",
)

#Fim do rodapé