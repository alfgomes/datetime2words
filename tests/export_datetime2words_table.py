# export_datetime2words_table.py
import csv
from datetime2words import datetime2words, date2words, time2words

def generate_table():
    languages = ["pt", "en", "fr"]
    datetime_examples = [
        "2025-11-03 15:40",
        "2025-11-03",
        "15:40",
        "03-11-2025 03:40PM"
    ]
    
    # Arquivos de saída
    csv_file = "datetime2words_output.csv"
    md_file = "datetime2words_output.md"

    # Preparando CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["Input", "Function", "Language", "Output"])
        
        for lang in languages:
            for dt_str in datetime_examples:
                writer.writerow([dt_str, "datetime2words", lang, datetime2words(dt_str, lang=lang)])
                writer.writerow([dt_str, "date2words", lang, date2words(dt_str, lang=lang)])
                writer.writerow([dt_str, "time2words", lang, time2words(dt_str, lang=lang)])
    
    # Preparando Markdown
    with open(md_file, mode='w', encoding='utf-8') as mdf:
        mdf.write("| Input | Function | Language | Output |\n")
        mdf.write("|-------|----------|---------|--------|\n")
        for lang in languages:
            for dt_str in datetime_examples:
                mdf.write(f"| {dt_str} | datetime2words | {lang} | {datetime2words(dt_str, lang=lang)} |\n")
                mdf.write(f"| {dt_str} | date2words     | {lang} | {date2words(dt_str, lang=lang)} |\n")
                mdf.write(f"| {dt_str} | time2words     | {lang} | {time2words(dt_str, lang=lang)} |\n")

    print(f"✅ Arquivos gerados: {csv_file} e {md_file}")

if __name__ == "__main__":
    generate_table()
