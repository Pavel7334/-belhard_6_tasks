"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n):
    if n < 10:
        return n
    return n % 10 + sum_of_numbers(n // 10)


foo = sum_of_numbers(23)
print(foo)

