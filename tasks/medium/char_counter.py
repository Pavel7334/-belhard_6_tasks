"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(str_val):
    char_counter = {}
    for char in str_val:
        if char not in char_counter.keys():
            char_counter[char] = 1
        else:
            char_counter[char] += 1

    return char_counter


count_char(STR_VAL)
