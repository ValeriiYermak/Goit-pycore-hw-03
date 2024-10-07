"""Завдання 2

Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали \
випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 \
чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних \
випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі \
випадкові числа в наборі повинні бути унікальні."""


import random

def get_numbers_ticket(quantity, min=1, max=1000):
    try:
        quantity = int(quantity)
        min = int(min)
        max = int(max)

        if quantity <=0:
            raise ValueError("Quantity must be a positive integer.")
        if min < 0:
            raise ValueError("Minimum number must be non-negative.")
        if min > max:
            raise ValueError("min cannot be greater than max.")
        if quantity > max - min + 1:
            raise ValueError(f"Quantity \"{quantity}\" cannot be greater than \"{max - min + 1}\"")
    except ValueError:
        print("Invalid input: Please enter valid integers numbers from 1 to 1000 for quantity, min, and max.")
        return None
    numbers = list(range(min, max + 1))
    return sorted(random.sample(numbers, quantity))

try:
    quantity_input = input("Enter the quantity of numbers: ")
    min_input = input("Enter the minimum number: ")
    max_input = input("Enter the maximum number: ")
    lottery_numbers = get_numbers_ticket(quantity_input, min_input, max_input)
    if lottery_numbers is not None:
        print("Your lottery numbers are: ", lottery_numbers)
except Exception as e:
    print("An error occurred:", e)



