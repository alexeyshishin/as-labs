#!/usr/bin/env python3

from lab7_1 import sum_1
from lab7_1 import sum_2

def select_operation(choise):
    if choise == 1:
        n = int(input("Введите параметр n для sum_1: "))
        return sum_1(n)
    elif choise == 2:
        n = int(input("Введите параметр n для sum_2: "))
        m = int(input("Введите параметр m для sum_2: "))
        return sum_2(n, m)
    else:
        raise ValueError("Неправильный ввод")

try:
    user_choice = int(input("Выбор операции (1 или 2): "))
    result = select_operation(user_choice)

    print(f"Результат вычисления: {result}")

except ValueError as e:
    print(f"Ошибка")