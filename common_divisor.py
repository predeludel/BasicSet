def common_divisor(first, second) -> int:
    flag = 0
    while flag == 0:
        subtraction = first - second
        if subtraction < second:
            first, second = second, subtraction
        elif subtraction > second:
            first, second = subtraction, second
        else:
            flag = second

    return flag


first, second = int((input('Введите первое число: '))), int((input('Введите первое число: ')))
first, second = max(first, second), min(first, second)
print(f"Наибольший общий делитель: {common_divisor(first, second)}")
