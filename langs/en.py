# languages/en.py
from num2words import num2words

# Set the default language for this module.
LANG = "en"

MONTHS = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
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
            suffix = "in the morning"
        elif 12 <= hour < 18:
            suffix = "in the afternoon"
        else:
            suffix = "in the evening"

        hour = hour % 12
        if hour == 0:
            hour = 12

    hour_text = num2words(hour, lang=LANG)
    
    # Monta o texto de minutos
    if show_minutes and minute != 0:
        minute_text = num2words(minute, lang=LANG)
        time_text = f"{hour_text} hours and {minute_text} minutes"
    else:
        time_text = f"{hour_text} hours"

    # Adiciona o sufixo se for 12h
    if hour_format == "12h":
        time_text += f" {suffix}"

    return time_text
