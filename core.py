import datetime
from num2words import num2words
from dateutil import parser
from datetime import datetime

# Função auxiliar para escolher idioma
def _load_lang_module(lang):
    if lang == 'pt':
        from .langs import pt as lang_mod
    elif lang == 'en':
        from .langs import en as lang_mod
    elif lang == 'fr':
        from .langs import fr as lang_mod
    else:
        from .langs import en as lang_mod
    return lang_mod

def parse_datetime(value):
    try:
        # Tenta parser geral
        return parser.parse(value, dayfirst=True)
    except Exception:
        # fallback para 12h AM/PM com dia-mês-ano
        fmts = [
            "%d-%m-%Y %I:%M%p",  # 03-11-2025 03:40PM
            "%d-%m-%Y %H:%M",    # 03-11-2025 15:40
            "%Y-%m-%d %H:%M",    # 2025-11-03 15:40
            "%Y-%m-%d",          # 2025-11-03
            "%H:%M",             # 15:40
        ]
        for fmt in fmts:
            try:
                return datetime.strptime(value, fmt)
            except:
                continue
        raise ValueError(f"Cannot parse date/time: {value}")




def datetime2words(value, lang=None, year_in_words=True, hour_format="24h", show_minutes=True):
    lang_mod = _load_lang_module(lang)
    try:
        # Tenta detectar datetime
        dt_obj = parse_datetime(value)

        # Montar saída
        if dt_obj.hour == 0 and dt_obj.minute == 0:
            return lang_mod.date2words(dt_obj, year_in_words=year_in_words)
        elif dt_obj.year == 1900:
            return lang_mod.time2words(dt_obj, hour_format=hour_format, show_minutes=show_minutes)
        return lang_mod.date2words(dt_obj, year_in_words=year_in_words) + ', ' + \
               lang_mod.time2words(dt_obj, hour_format=hour_format, show_minutes=show_minutes)
    except Exception as e:
        return str(e)


def date2words(value, lang=None, year_in_words=True):
    lang_mod = _load_lang_module(lang)
    try:
        dt_obj = datetime.datetime.strptime(value, '%Y-%m-%d')
        return lang_mod.date2words(dt_obj, year_in_words=year_in_words)
    except:
        return datetime2words(value, lang=lang, year_in_words=year_in_words).split(',')[0]


def time2words(value, lang=None, hour_format="24h", show_minutes=True):
    lang_mod = _load_lang_module(lang)
    try:
        dt_obj = parse_datetime(value)
        return lang_mod.time2words(dt_obj, hour_format=hour_format, show_minutes=show_minutes)
    except:
        parts = value.split()
        if len(parts) == 2 and ('AM' in parts[1] or 'PM' in parts[1]):
            dt_obj = datetime.datetime.strptime(value, '%I:%M%p')
            return lang_mod.time2words(dt_obj, hour_format=hour_format, show_minutes=show_minutes)
        return datetime2words(value, lang=lang, hour_format=hour_format, show_minutes=show_minutes).split(',')[-1]
