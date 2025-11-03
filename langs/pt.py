# languages/pt.py
from num2words import num2words

# Define a língua padrão deste módulo
LANG = "pt"

MONTHS = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}

def date2words(dt_obj, year_in_words=True):
    day = num2words(dt_obj.day, lang=LANG)
    month = MONTHS[dt_obj.month]
    if year_in_words:
        year = num2words(dt_obj.year, lang=LANG)
    else:
        year = str(dt_obj.year)
    return f"{day} de {month} de {year}"

def time2words(dt_obj, hour_format="24h", show_minutes=True):
    hour = dt_obj.hour
    minute = dt_obj.minute
    suffix = ""

    # Ajuste formato 12h
    if hour_format == "12h":
        if 0 <= hour < 12:
            suffix = "da manhã"
        elif 12 <= hour < 18:
            suffix = "da tarde"
        else:
            suffix = "da noite"

        hour = hour % 12
        if hour == 0:
            hour = 12

    hour_text = num2words(hour, lang=LANG)
    
    if show_minutes:
        minute_text = num2words(minute, lang=LANG)
        return f"{hour_text} horas e {minute_text} minutos" if minute != 0 else f"{hour_text} horas"
    else:
        return f"{hour_text} horas" + (f" {suffix}" if hour_format == "12h" else "")
