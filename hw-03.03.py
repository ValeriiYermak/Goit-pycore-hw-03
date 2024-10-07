"""
У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. Для цього ви збираєте телефонні
номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах. Наприклад:

"    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "

Ваш сервіс розсилок може ефективно відправляти повідомлення лише тоді, коли номери телефонів представлені у коректному
форматі. Тому вам необхідна функція, яка автоматично нормалізує номери телефонів до потрібного формату, видаляючи всі
зайві символи та додаючи міжнародний код країни, якщо потрібно.

Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи
тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі
та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду,
функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.
"""

import re


def normalize_phone(phone_number):

    normalized_number = re.sub(r'[^\d+]', '', phone_number)

    if normalized_number.startswith('+'):
        if normalized_number.startswith('+380'):
            return normalized_number
        elif normalized_number.startswith('+38'):
            return normalized_number
        elif normalized_number.startswith('+0'):
            return '+38' + normalized_number[2:]
        else:
            return normalized_number
    elif normalized_number.startswith('0'):
        normalized_number = '+38' + normalized_number[1:]
    elif normalized_number.startswith('380'):
        normalized_number = '+' + normalized_number[2:]
    else:
        normalized_number = '+38' + normalized_number
    if normalized_number.startswith('+0'):
        normalized_number = '+38' + normalized_number[2:]
    return normalized_number


phone_numbers = [
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11",
    "+380123456789",
    "0123456789",
]

for number in phone_numbers:
    print(normalize_phone(number))