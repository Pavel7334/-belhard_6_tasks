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


# def sum_of_numbers(num):
#     sum_integers = 0
#     for num in nums:
#         if isinstance(num, int):
#             sum_integers += num
#         return sum_of_numbers(num + num)

