import itertools
import time

import sympy

primes = [2]


def prime_ways(n):
    for i in range(primes[-1] + 1, n + 1):
        if sympy.isprime(i):
            primes.append(i)
    ways = [1] + [0] * n
    for p in primes:
        for i in range(n + 1 - p):
            ways[i + p] += ways[i]
    return ways[n]


def solve(target):
    return next(filter(lambda n: prime_ways(n) > target, itertools.count(2)))


srt = time.time()
answer = solve(5000)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
