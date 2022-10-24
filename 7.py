import math


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


prime_count = 1
n = 2
while prime_count < 10001:
    n += 1
    if is_prime(n):
        prime_count += 1
print(n)
