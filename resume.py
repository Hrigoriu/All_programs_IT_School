def print_resume(resume_data):
    """Моє резюме"""

    # Розміри колонок
    col_widths = {
        "Ім'я": 14,
        "Дата народження": 15,
        "Адреса": 25,
        "Навчання": 15,
        "Робота": 10,
        "Сім'я": 19,
        "Досягнення": 15,
        "Хобі": 10,
    }

    # Заголовки колонок
    header = ""
    for col_name, width in col_widths.items():
        header += f"{col_name:{width}} | "
    print(header.rstrip(" | "))  # Поперечка розділу колонок
    print("-" * len(header))     # Лінія розділу

    # Колонки
    for person in resume_data:
        row = ""
        for col_name, width in col_widths.items():
            value = person.get(col_name, "")  # Значення
            row += f"{value:{width}} | "
        print(row.rstrip(" | "))

# Мої дані
resume_data = [
    {
        "Ім'я": "Григорій Шаров",
        "Дата народження": "1984-31-01",
        "Адреса": "Харків, 13 Весняна, кв.13",
        "Навчання": "IT Step school",
        "Робота": "Програміст",
        "Сім'я": "Одружений, 1 дитина",
        "Досягнення": "Ухилянт))",
        "Хобі": "Кодити))",
    },
]

print_resume(resume_data)