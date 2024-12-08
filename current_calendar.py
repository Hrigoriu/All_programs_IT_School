import calendar
from datetime import datetime

#  Введення правильної дати: рік, місяць
current_year = datetime.now().year
current_month = datetime.now().month

# Виведення календаря
print(calendar.month(current_year, current_month))