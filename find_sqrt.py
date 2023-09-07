def find_sqrt(num):
    flag = "Слишком сложно, не могу!"
    for i in range(num // 2 + 2):
        if i * i == num:
            flag = i
            break
    return flag


print(f"Ответ: {find_sqrt(int(input('Введите число: ')))}")
