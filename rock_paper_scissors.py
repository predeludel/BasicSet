first_player, second_player = str(input("Введите два слова:")).split(" ")

words = ["", "камень", "ножницы", "бумага"]


def find_winner(first, second):
    if first in words and second in words:
        summ = words.index(first) - words.index(second)
        if -2 < summ < 0 or summ == 2:
            return "игрок 1 выиграл"
        elif 2 > summ > 0 or summ == -2:
            return "игрок 2 выиграл"
        else:
            return "ничья"
    return "вы проиграли - для игры нужны лишь: камень, ножницы, бумага"


print(find_winner(first_player, second_player))
