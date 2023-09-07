def square_array(value):
    square = [i ** 2 for i in range(-1 * value, value + 1)]
    return square


print(square_array(int(input("Введите число: "))))
