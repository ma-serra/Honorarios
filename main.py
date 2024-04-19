import streamlit as st
import pandas as pd

# Título do aplicativo
st.title('Calculadora de Honorários Advocatícios')

# Entrada de dados
valor_total_creditado = st.number_input('Insira o valor total creditado na conta do escritório (R$)', min_value=0.0, format='%f')
porcentagem_sucumbencia = st.number_input('Insira a porcentagem dos honorários de sucumbência (%)', min_value=0.0, format='%f')
porcentagem_contratual = st.number_input('Insira a porcentagem dos honorários contratuais (%)', min_value=0.0, format='%f')

if st.button('Calcular'):
    # Ajustando o cálculo para considerar que a porcentagem de sucumbência se aplica sobre a condenação
    valor_condenacao = valor_total_creditado / (1 + porcentagem_sucumbencia / 100)

    # Calculando o valor dos honorários de sucumbência
    honorarios_sucumbencia = valor_condenacao * (porcentagem_sucumbencia / 100)

    # Calculando honorários contratuais sobre a condenação
    honorarios_contratuais = valor_condenacao * (porcentagem_contratual / 100)

    # Calculando o valor a ser transferido para a parte
    valor_para_parte = valor_condenacao - honorarios_contratuais

    # Valor que restará ao escritório
    valor_escritorio = honorarios_sucumbencia + honorarios_contratuais

    # Dividindo o total de honorários por dois
    divisao_honorarios = valor_escritorio / 2

    # Função para formatar valores monetários
    def formatar_valor(valor):
        return f'R$ {valor:,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.')

    # Preparando dados para exibição em tabela
    dados = {
        'Descrição': ['Honorários de Sucumbência', 'Valor da Condenação', 'Honorários Contratuais',
                      'Valor a ser transferido para a parte', 'Valor restante ao escritório', 'Metade dos Honorários Totais'],
        'Valor': [formatar_valor(honorarios_sucumbencia),
                  formatar_valor(valor_condenacao),
                  formatar_valor(honorarios_contratuais),
                  formatar_valor(valor_para_parte),
                  formatar_valor(valor_escritorio),
                  formatar_valor(divisao_honorarios)]
    }

    tabela = pd.DataFrame(dados)
    st.table(tabela)
