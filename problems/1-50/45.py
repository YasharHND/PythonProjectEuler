import math


def triangle(n):
    return (n * (n + 1)) // 2


# https://stackoverflow.com/a/37390529/19581178
def is_pentagonal(n):
    k = (math.sqrt(24 * n + 1) + 1) / 6
    return k.is_integer()


def is_hexagonal(n):
    k = (math.sqrt(8 * n + 1) + 1) / 4
    return k.is_integer()


i = 286
while True:
    ti = triangle(i)
    if is_pentagonal(ti) and is_hexagonal(ti):
        print(ti)
        break
    i += 1
