# datetime2words
A Python package for converting dates and times into words (in full) in multiple languages.

## Installation

```
bash
git clone https://github.com/alfgomes/datetime2words.git
cd datetime2words
pip install .
```

## Usage Examples

```
python
from datetime2words import datetime2words, date2words, time2words

print(datetime2words("2025-11-03 15:40", lang="pt"))
# três de novembro de dois mil e vinte e cinco, quinze horas e quarenta minutos

print(date2words("2025-11-03", lang="pt"))
# três de novembro de dois mil e vinte e cinco

print(time2words("15:40", lang="pt"))
# quinze horas e quarenta minutos
```