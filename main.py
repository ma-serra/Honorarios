import re

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Calculadora de Honorários Adv!",
                   layout="centered")


# Função para validar o número do processo
def validar_processo(numero):
  # Regex para verificar o formato: 0123456-00.2099.8.05.0001
  pattern = r'^\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}$'
  return re.match(pattern, numero) is not None


# Título do aplicativo
st.title('_Calculadora de Honorários Advocatícios_', anchor=False)
st.divider()

# Entrada de dados
processo = st.text_input('Insira o número do processo:',
                         placeholder='Ex: 0123456-00.2099.8.05.0001')
autor = st.text_input('Insira o nome do autor:', placeholder='Nome do autor.')
valor_total_creditado = st.number_input(
    'Insira o valor total creditado na conta do escritório (R$)',
    min_value=0,
    placeholder='R$ 0,00')

porcentagem_sucumbencia = st.number_input(
    'Insira a porcentagem dos honorários de sucumbência (%)',
    min_value=0,
    placeholder='%')
porcentagem_contratual = st.number_input(
    'Insira a porcentagem dos honorários contratuais (%)',
    min_value=0,
    placeholder='%')
quantidade_advogados = st.number_input('Insira a quantidade de advogados',
                                       min_value=1)

if st.button('Calcular'):
  if valor_total_creditado == 0:
    st.error(
        'O valor total creditado não pode ser zero. Cálculo não realizado.')
  if processo:
    if validar_processo(processo):
      st.success("Número do processo válido!", icon="✅")

    else:
      st.error(
          "Formato inválido! Por favor, insira o número no formato 0123456-00.2099.8.05.0001."
      )

    # Calculando a sucumbência sobre a condenação.
    valor_condenacao = valor_total_creditado / (1 +
                                                porcentagem_sucumbencia / 100)

    # Calculando o valor dos honorários de sucumbência
    honorarios_sucumbencia = valor_condenacao * (porcentagem_sucumbencia / 100)

    # Calculando honorários contratuais sobre a condenação
    honorarios_contratuais = valor_condenacao * (porcentagem_contratual / 100)

    # Calculando o valor a ser transferido para a parte
    valor_para_parte = valor_condenacao - honorarios_contratuais

    # Valor que restará ao escritório
    valor_escritorio = honorarios_sucumbencia + honorarios_contratuais

    # Dividindo o total de honorários pela quantidade de advogados
    divisao_honorarios = valor_escritorio / quantidade_advogados

    # Função para formatar valores monetários
    def formatar_valor(valor):
      return f'R$ {valor:,.2f}'.replace(',',
                                        'x').replace('.',
                                                     ',').replace('x', '.')

    dados = {
        'Descrição': [
            'Valor depositado:',
            f'Honorários de Sucumbência: ({porcentagem_sucumbencia}%.)',
            'Valor da Condenação:',
            f'Honorários Contratuais: ({porcentagem_contratual}% sobre a condenação.)',
            'Valor a ser transferido para a parte:',
            'Valor restante do escritório:',
            f'Valor para cada advogado: ({quantidade_advogados})'
        ],
        'Valor': [
            formatar_valor(valor_total_creditado),
            formatar_valor(honorarios_sucumbencia),
            formatar_valor(valor_condenacao),
            formatar_valor(honorarios_contratuais),
            formatar_valor(valor_para_parte),
            formatar_valor(valor_escritorio),
            formatar_valor(divisao_honorarios)
        ]
    }

    st.divider()

    st.write(f'Processo nº: {processo}')
    st.write(f'Autor: **{autor}**')
    tabela = pd.DataFrame(dados)
    st.table(tabela)

    # Cria a string de cabeçalho personalizada com as variáveis globais
    header_string = f"Processo nº: {processo}.\nAutor: {autor}.\n"

    # Converte DataFrame para CSV
    csv_data = tabela.to_csv(index=False)

    # Concatena o cabeçalho personalizado com os dados do CSV
    full_csv = header_string + csv_data

    # Converte para bytes incluindo o BOM
    csv_bytes = ('\ufeff' + full_csv).encode('utf-8')

    # Botão para baixar a tabela como CSV
    st.download_button(label='Baixar tabela',
                       data=csv_bytes,
                       file_name='tabela.csv',
                       mime='text/csv')

    st.divider()
