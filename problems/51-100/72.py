import math
import time
from fractions import Fraction

import sympy
from sortedcontainers import SortedSet


def count_by_generating(limit):
    sequence = SortedSet()
    for d in range(2, limit + 1):
        for n in range(1, d):
            if math.gcd(n, d) == 1:
                sequence.add(Fraction(n, d))
    return len(sequence)


def totient(n):
    product = n
    for factor in sympy.primefactors(n):
        product *= 1 - (1 / factor)
    return math.floor(product)


def sample():
    for i in range(2, 11):
        print(i, count_by_generating(i), totient(i))


def solve(d):
    return sum(totient(n) for n in range(2, d + 1))


sample()

srt = time.time()
answer = solve(10 ** 6)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
