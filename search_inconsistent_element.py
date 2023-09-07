def search_element(list):
    index = [i + 1 for i in range(len(list) - 1) if (int(list[i + 1]) - int(list[i])) > 1]
    if len(index) == 0:
        return "Не найдено"
    return index


print(search_element(input("Введите массив: ").split(",")))
