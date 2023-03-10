"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(numbers):
    used = set()
    for i in numbers:
        if i in used:
            print('Yes')
        else:
            print('No')
            used.add(i)
