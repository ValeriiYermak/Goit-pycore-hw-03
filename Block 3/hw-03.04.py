"""
Завдання 4

У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес,
вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати.
Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день
народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та
переносити дату привітання на наступний робочий день, якщо необхідно.
"""

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.now().date()

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= today + timedelta(days=7):
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John", "birthday": "1990.10.11"},
    {"name": "Jane", "birthday": "1995.10.08"},
    {"name": "Bob", "birthday": "2000.10.12"},
    {"name": "Alice", "birthday": "2002.10.14"},
    {"name": "Charlie", "birthday": "2010.01.01"},
    {"name": "David", "birthday": "2015.01.01"},
    {"name": "Eve", "birthday": "2020.10.16"},
]

result = get_upcoming_birthdays(users)
print(result)



