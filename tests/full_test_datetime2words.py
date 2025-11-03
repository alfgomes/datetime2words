# full_test_datetime2words.py
from datetime2words import datetime2words, date2words, time2words

def run_full_tests():
    languages = ["pt", "en", "fr"]
    
    print("===== Teste completo do pacote datetime2words =====\n")
    
    for lang in languages:
        print(f"--- Idioma: {lang} ---")
        
        print("\n**Testando datas do mês (1 a 5) em 2025-11**")
        for day in range(1, 6):
            date_str = f"2025-11-{day:02d}"
            print(f"{date_str} -> {date2words(date_str, lang=lang)}")
        
        print("\n**Testando horários do dia em intervalos de 15 minutos**")
        for hour in range(0, 24, 6):
            for minute in [0, 15, 30, 45]:
                time_str = f"{hour:02d}:{minute:02d}"
                print(f"{time_str} -> {time2words(time_str, lang=lang)}")
        
        print("\n**Testando combinações de data e hora**")
        datetime_examples = [
            "2025-11-03 15:40",
            "2025-11-03",
            "15:40",
            "03-11-2025 03:40PM"
        ]
        for dt_str in datetime_examples:
            print(f"{dt_str} -> {datetime2words(dt_str, lang=lang)}")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    run_full_tests()
