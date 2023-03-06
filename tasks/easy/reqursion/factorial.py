"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(num):
    if num == 1:
        return 1
    return factorial(num - 1) * num


factorial(1)
