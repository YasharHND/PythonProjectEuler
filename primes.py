import math


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return False
    return True


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
