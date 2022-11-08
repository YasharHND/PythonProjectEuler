import math


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


print(2 + sum(n for n in range(3, 2000000) if is_prime(n)))
