from functools import reduce
from itertools import permutations


primes = [2, 3, 5, 7, 11, 13, 17]


def is_sub_divisible(number):
    for i in range(1, 8):
        prime = primes[i - 1]
        sub_number = int(number[i:i + 3])
        if sub_number % prime != 0:
            return False
    return True


summation = 0
for permutation in permutations(range(10)):
    if permutation[0] == 0:
        continue
    str_number = reduce(lambda x, y: str(x) + str(y), permutation)
    if is_sub_divisible(str_number):
        summation += int(str_number)
print(summation)
