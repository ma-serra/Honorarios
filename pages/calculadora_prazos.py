import streamlit as st
import datetime
import pandas as pd
import holidays

# Mapeamento dos dias da semana para português do Brasil
DAYS_PT_BR = {
    "Monday": "Segunda",
    "Tuesday": "Terça",
    "Wednesday": "Quarta",
    "Thursday": "Quinta",
    "Friday": "Sexta",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

def is_working_day(date, br_holidays):
    return date.weekday() < 5 and date not in br_holidays

def next_working_day(date, br_holidays):
    next_day = date + datetime.timedelta(days=1)
    while not is_working_day(next_day, br_holidays):
        next_day += datetime.timedelta(days=1)
    return next_day

def add_working_days(start_date, days_to_add, br_holidays):
    current_date = start_date
    while days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        if is_working_day(current_date, br_holidays):
            days_to_add -= 1
    return current_date

def calculate_deadline(disponibilizacao_date, days, br_holidays):
    publicacao_date = next_working_day(disponibilizacao_date, br_holidays)
    start_date = publicacao_date + datetime.timedelta(days=1)
    if not is_working_day(start_date, br_holidays):
        start_date = next_working_day(start_date, br_holidays)
    end_date = add_working_days(start_date, days - 1, br_holidays)
    return publicacao_date, start_date, end_date

def get_event_description(date, br_holidays, disponibilizacao_date, publicacao_date):
    if date.date() == disponibilizacao_date:
        return "Data da Disponibilização"
    elif date.date() == publicacao_date:
        return "Data da Publicação"
    elif date.weekday() == 5:
        return "Sábado"
    elif date.weekday() == 6:
        return "Domingo"
    elif date.date() in br_holidays:
        return f"Feriado: {br_holidays.get(date.date())}"
    return "Dia Útil"

def get_day_name_pt_br(date):
    day_name = date.strftime('%A')
    return DAYS_PT_BR[day_name]

def main():
    st.image("Bandeira_da_Bahia.svg", width=50)
    st.title("Calculadora de Prazos: Bahia!")
    
    br_holidays = holidays.BR(state='BA')

    disponibilizacao_date = st.date_input(
        "Data da disponibilização no Diário",
        datetime.date.today(),
        format="DD/MM/YYYY"
    )
    days = st.number_input("Número de Dias", min_value=1, value=15)

    if st.button("Calcular"):
        publicacao_date, start_date, end_date = calculate_deadline(disponibilizacao_date, days, br_holidays)

        st.success(f"""
        Data da Disponibilização no DJE: {disponibilizacao_date.strftime('%d/%m/%Y')} - {get_day_name_pt_br(disponibilizacao_date)}\n
        Data da Publicação: {publicacao_date.strftime('%d/%m/%Y')} - {get_day_name_pt_br(publicacao_date)}\n
        Data Inicial do Prazo: {start_date.strftime('%d/%m/%Y')} - {get_day_name_pt_br(start_date)}\n
        Data Final: {end_date.strftime('%d/%m/%Y')} - {get_day_name_pt_br(end_date)}\n
        """)

        st.subheader("Detalhes dos Dias Úteis")

        date_range = pd.date_range(start=disponibilizacao_date, end=end_date)
        details = []
        day_count = 0

        for date in date_range:
            event = get_event_description(date, br_holidays, disponibilizacao_date, publicacao_date)

            if is_working_day(date.date(), br_holidays) and date.date() >= start_date:
                day_count += 1
                day_of_term = str(day_count)
            else:
                day_of_term = "-"

            details.append({
                "Data": date.strftime('%d/%m/%Y') + " - " + get_day_name_pt_br(date),
                "Dia do Prazo": day_of_term,
                "Evento": event
            })

        df = pd.DataFrame(details)
        st.table(df)

if __name__ == "__main__":
    main()