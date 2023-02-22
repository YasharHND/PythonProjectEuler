import math

from modules.primes import is_prime


def is_end_of_circle(number):
    return number % 2 != 0 and math.isqrt(number) ** 2 == number


n = 1
c = 1
prime_count = 0
diagonal_count = 1
while True:
    if is_end_of_circle(n):
        c += 1
    n += 2 * (c - 1)
    diagonal_count += 1
    if is_prime(n):
        prime_count += 1
    if prime_count / diagonal_count < 0.1:
        print((c * 2) - 1)
        break
