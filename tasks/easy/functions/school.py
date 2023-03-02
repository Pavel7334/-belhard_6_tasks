"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""


def incr_students(data, name):
    data[name] += 1
    return data


def decr_students(data, name):
    if data.get(name, 0) > 0:
        data[name] -= 1


def add_class(data, name):
    data.update({name: 0})


def remove_class(data, name):
    data.pop(name, None)


def calc_students(data):
    return sum(data.values())


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}