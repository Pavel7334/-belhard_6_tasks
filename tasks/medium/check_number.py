"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return check_number(n // 2)


check_number(10)
print(check_number(10))







    # return True if (n & (n - 1)) == 0 else False      # 1-e решение



    # if num == 1:                                      2-e решение
    #     return True
    # if num & 1:
    #     return False
    # return check_number(num >> 1)
