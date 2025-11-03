# languages/fr.py
from num2words import num2words

# Définissez la langue par défaut pour ce module.
LANG = "fr"

MONTHS = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril",
    5: "mai", 6: "juin", 7: "juillet", 8: "août",
    9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"
}

def date2words(dt_obj, year_in_words=True):
    day = num2words(dt_obj.day, lang=LANG)
    month = MONTHS[dt_obj.month]
    if year_in_words:
        year = num2words(dt_obj.year, lang=LANG)
    else:
        year = str(dt_obj.year)
    return f"{day} {month} {year}"

def time2words(dt_obj, hour_format="24h", show_minutes=True):
    hour = dt_obj.hour
    minute = dt_obj.minute
    suffix = ""

    if hour_format == "12h":
        if 0 <= hour < 12:
            suffix = "du matin"
        elif 12 <= hour < 18:
            suffix = "de l'après-midi"
        else:
            suffix = "du nuit"

        hour = hour % 12
        if hour == 0:
            hour = 12


    hour_text = num2words(hour, lang=LANG)

    if show_minutes:
        minute_text = num2words(minute, lang=LANG)
        return f"{hour_text} heures et {minute_text} minutes" if minute != 0 else f"{hour_text} heures"
    else:
        return f"{hour_text} heures" + (f" {suffix}" if hour_format == "12h" else "")
