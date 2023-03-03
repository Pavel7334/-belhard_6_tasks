"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""
import math


def get_even_number():
    a = 0
    while True:
        a += 2
        yield a


get_even_number()
