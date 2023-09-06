import math


def full_amount(N):
    Sn3 = find_amount(3, N)
    Sn5 = find_amount(5, N)
    Sn15 = find_amount(15, N)
    return Sn3 + Sn5 - (2 * Sn15)


def find_amount(d, N):
    Sn = ((d + (round((N - (N % d)), 0))) / 2) * math.floor((N) / d)
    return Sn


n = int(input('Число N = '))
print(full_amount(n))
