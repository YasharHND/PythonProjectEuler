import math
from functools import reduce


def prime_factors_powers(n):
    last_factor = None
    out = []
    # Print the number of two's that divide
    while n % 2 == 0:
        if last_factor == 2:
            out[-1] += 1
        else:
            last_factor = 2
            out.append(1)
        n = n / 2
    # n must be odd at this point
    # so a skip of 2 (i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i and divide n
        while n % i == 0:
            if last_factor == i:
                out[-1] += 1
            else:
                last_factor = i
                out.append(1)
            n = n / i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        out.append(1)
    return out


def count_divisors(number):
    return reduce(lambda x, y: x * y, [n + 1 for n in prime_factors_powers(number)])


triangle = 3
step = 3
while True:
    if count_divisors(triangle) > 500:
        print(triangle)
        break
    triangle += step
    step += 1
