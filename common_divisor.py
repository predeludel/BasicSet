# from typing import TypeAlias
#
# IntOrNone: TypeAlias = int | None


def common_divisor(first, second) -> int:
    flag = 0
    while flag == 0:
        subtraction = first - second
        if subtraction > second:
            while subtraction > second:
                subtraction = first - second
                first = subtraction
        if subtraction == 0:
            flag = second
        first, second = second, subtraction
    return flag


first, second = int((input('Введите первое число: '))), int((input('Введите первое число: ')))
print(f"Наибольший общий делитель: {common_divisor(first, second)}")
