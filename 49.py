import itertools
import math
from functools import reduce
from itertools import product


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_another_permutation(p, n):
    return sorted(p) == sorted([int(d) for d in str(n)])


for permutation in product(range(10), repeat=4):
    if permutation[0] == 0:
        continue
    if permutation == (1, 4, 8, 7):
        continue
    n1 = int(reduce(lambda x, y: str(x) + str(y), permutation))
    if is_prime(n1):
        n2 = n1 + 3330
        if is_prime(n2) and is_another_permutation(permutation, n2):
            n3 = n2 + 3330
            if is_prime(n3) and is_another_permutation(permutation, n3):
                print(f"{n1}{n2}{n3}")
                break
