import math
from functools import reduce
from itertools import permutations


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


for digit in reversed(range(2, 10)):
    for permutation in permutations(reversed(range(1, digit + 1))):
        n = int(reduce(lambda x, y: str(x) + str(y), permutation))
        if is_prime(n):
            print(n)
            break
    else:
        continue
    break
