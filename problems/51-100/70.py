import math
import time
from fractions import Fraction

import sympy


# https://www.youtube.com/watch?v=ndObjfFXhB0
# https://en.wikipedia.org/wiki/Euler%27s_totient_function
def solve(limit):
    target_n = 0
    min_ratio = math.inf
    max_limit = sympy.prevprime(math.sqrt(limit) * 1.5)
    prime_upper = 3
    while prime_upper < max_limit:
        prime_lower = 2
        while prime_lower < prime_upper:
            product = prime_lower * prime_upper
            if product > limit:
                break
            totient = math.floor(product * (1 - 1 / prime_lower) * (1 - 1 / prime_upper))
            ratio = Fraction(product, totient)
            if ratio < min_ratio and sorted(str(product)) == sorted(str(totient)):
                target_n = product
                min_ratio = ratio
            prime_lower = sympy.nextprime(prime_lower)
        prime_upper = sympy.nextprime(prime_upper)
    return target_n


srt = time.time()
answer = solve(10 ** 7)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
