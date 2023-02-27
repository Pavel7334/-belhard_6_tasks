"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):

    if not all(type(arg) == int or type(arg) == float for arg in args):
        raise TypeError("Все позиционные аргументы должны быть целыми")
    args_sum = sum(args)

    if not all(type(kwarg) == str and type(value) == str for kwarg, value in kwargs.items()):
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    new_list = list(kwargs.keys()) + list(kwargs.values())
    kwargs_max_len = len(max(new_list, key=len))

    return {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len,
    }
