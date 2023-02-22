from functools import reduce
from itertools import permutations

from modules.primes import is_prime

for digit in reversed(range(2, 10)):
    for permutation in permutations(reversed(range(1, digit + 1))):
        n = int(reduce(lambda x, y: str(x) + str(y), permutation))
        if is_prime(n):
            print(n)
            break
    else:
        continue
    break
