first_player, second_player = str(input("Введите два слова:")).split(" ")

words = ["ничья", "камень", "ножницы", "бумага"]


def find_winner(first, second):
    summ = words.index(first) - words.index(second)
    if -2 < summ < 0 or summ == 2:
        return "игрок 1 выиграл"
    elif 2 > summ > 0 or summ == -2:
        return "игрок 2 выиграл"
    else:
        return


print(find_winner(first_player, second_player))
