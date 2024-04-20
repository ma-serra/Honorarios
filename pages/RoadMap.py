# RoadMap.py
import streamlit as st
import main
from proximospassos import get_proximos_passos

st.set_page_config("Calculadora de Honorários Advocatícios!", "calculadora_svg.svg")

main.sidebar()

st.image("calculadora_svg.svg", width=75)

st.write(
    """
    # Calculadora de Honorários Advocatícios!\n\n
    Bem-vindo ao nosso roteiro (roadmap)! 👋\n 
    Esta página mostra algumas melhorias que pretendemos implementar neste projeto.\n 
    Além disso, sempre há mais acontecendo nos bastidores — às vezes gostamos de surpreendê-los.✨
    """
)

# Aqui vamos exibir os próximos passos do roadmap
st.markdown(get_proximos_passos())

st.info(
    """
    Tem alguma sugestão ou ideia? 
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

