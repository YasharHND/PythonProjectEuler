import math


def distinct_prime_factors(number):
    out = set()
    if number % 2 == 0:
        out.add(2)
    while number % 2 == 0:
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            out.add(i)
            number = number / i
    if number > 2:
        out.add(int(number))
    return out
