import os

# Limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# test_datetime2words.py
from datetime2words import datetime2words, date2words, time2words

def run_tests():
    print("======================================== Teste básico usando locale do sistema =========================================")
    print("datetime2words completo           :", datetime2words("2025-11-03 15:40"))
    print("date2words (ano numérico)         :", date2words("2025-11-03", year_in_words=False))
    print("date2words (ano por extenso)      :", date2words("2025-11-03"))
    print("time2words completo               :", time2words("15:40"))
    print("time2words só hora (24h)          :", time2words("15:00"))
    print("time2words só hora (12h)          :", time2words("03:40PM", hour_format="12h"))
    print("time2words só hora sem minutos    :", time2words("03:00PM", hour_format="12h"))

    print("\n============================================== Teste com idioma explícito ==============================================")
    print("datetime2words (pt)               :", datetime2words("2025-11-03 15:40", lang="pt"))
    print("date2words (en)                   :", date2words("2025-11-03", lang="en"))
    print("time2words (fr, formato 12h)      :", time2words("15:40", lang="fr", hour_format="12h"))
    print("time2words (en, formato 12h)      :", time2words("03:40PM", lang="en", hour_format="12h"))

    print("\n==================================== Teste com datas parciais e formatos diferentes ====================================")
    print("datetime2words só hora            :", datetime2words("15:40"))
    print("datetime2words só data            :", datetime2words("2025-11-03"))
    print("datetime2words 12h com data US    :", datetime2words("03-11-2025 03:40PM", lang="pt"))
    print("datetime2words 12h com data EN    :", datetime2words("11/03/2025 03:40PM", lang="en"))

    print("\n=========================================== Teste com formatos alternativos ===========================================")
    print("datetime2words curto YY-MM-DD     :", datetime2words("25-11-03 15:40", lang="pt"))
    print("datetime2words ISO com T          :", datetime2words("2025-11-03T15:40", lang="pt"))
    print("datetime2words só minutos zero    :", datetime2words("15:00", lang="pt"))
    print("time2words 24h, sem minutos       :", time2words("15:00", hour_format="24h"))
    print("time2words 12h, sem minutos       :", time2words("03:00PM", hour_format="12h"))

    print("\n=================================================== Teste de erros ===================================================")
    print("datetime2words inválido           :", datetime2words("não é data", lang="pt"))
    print("time2words inválido               :", time2words("99:99", lang="en"))

if __name__ == "__main__":
    run_tests()
