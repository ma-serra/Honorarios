import pandas as pd
import streamlit as st
import functions

functions.página_inicial()
functions.sidebar()

# Entrada de dados
processo = st.text_input('Insira o número do processo:', placeholder='Ex: 0123456-00.2099.8.05.0001')
autor = st.text_input('Insira o nome do autor:', placeholder='Nome do autor.')
valor_total_creditado = st.number_input('Insira o valor total creditado na conta do escritório (R$):', placeholder='R$ 0,00')
porcentagem_sucumbencia = st.number_input('Insira a porcentagem dos honorários de sucumbência (%):', min_value=0)
porcentagem_contratual = st.number_input('Insira a porcentagem dos honorários contratuais (%):', min_value=0)
quantidade_advogados = st.number_input('Insira a quantidade de advogados', min_value=1)

# Botão de cálculo e lógica
if st.button('Calcular'):
    try:
        st.write("Valor formatado:", functions.formatar_valor(valor_total_creditado))
    except ValueError:
        st.error("Por favor, insira um número válido para o valor total creditado.")

    if functions.validar_processo(processo):
        # Restante do código de cálculo, assumindo que o valor total e o número do processo são válidos.
        pass
    else:
        st.error("Formato inválido! Por favor, insira o número no formato 0123456-00.2099.8.05.0001.")


    # Calculando a sucumbência sobre a condenação.
    valor_condenacao = valor_total_creditado / (1 + porcentagem_sucumbencia / 100)

    # Calculando o valor dos honorários de sucumbência
    honorarios_sucumbencia = functions.calcular_honorario(valor_condenacao,
                                                porcentagem_sucumbencia)

    # Calculando honorários contratuais sobre a condenação
    honorarios_contratuais = functions.calcular_honorario(valor_condenacao,
                                                porcentagem_contratual)

    # Calculando o valor a ser transferido para a parte
    valor_para_parte = valor_condenacao - honorarios_contratuais

    # Valor que restará ao escritório
    valor_escritorio = honorarios_sucumbencia + honorarios_contratuais

    # Dividindo o total de honorários pela quantidade de advogados
    divisao_honorarios = valor_escritorio / quantidade_advogados

    # Criando tabela com os resultados

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
            functions.formatar_valor(valor_total_creditado),
            functions.formatar_valor(honorarios_sucumbencia),
            functions.formatar_valor(valor_condenacao),
            functions.formatar_valor(honorarios_contratuais),
            functions.formatar_valor(valor_para_parte),
            functions.formatar_valor(valor_escritorio),
            functions.formatar_valor(divisao_honorarios)
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
    
    st.download_button(label='Baixar tabela', data=csv_bytes, file_name='tabela.csv', mime='text/csv')
    
    st.divider()
