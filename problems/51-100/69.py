import math
import time

from modules.primes import distinct_prime_factors


# https://en.wikipedia.org/wiki/Euler%27s_totient_function
def totient(number):
    product = number
    for factor in distinct_prime_factors(number):
        product *= 1 - (1 / factor)
    return math.ceil(product)


def solve():
    target_n = 0
    maximum = 0
    for n in range(2, 1_000_001):
        n_tn = n / totient(n)
        if n_tn > maximum:
            maximum = n_tn
            target_n = n
    return target_n


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
