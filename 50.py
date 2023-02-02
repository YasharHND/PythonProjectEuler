import math


primes = [2, 3]


def is_prime(n):
    for i in range(3, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def get_prime(idx):
    while len(primes) <= idx:
        k = primes[-1]
        while True:
            k += 2
            if is_prime(k):
                primes.append(k)
                break
    return primes[idx]


def sum_of_primes(start, end):
    return sum(get_prime(idx) for idx in range(start, end))


limit = 1000000
target = 2
max_count = 1
last_idx = 0
while primes[-max_count] < limit:
    count = max_count + 1
    while True:
        summation = sum_of_primes(last_idx, last_idx + count)
        if summation >= limit:
            last_idx += 1
            break
        if summation % 2 != 0 and is_prime(summation):
            max_count = count
            target = summation
        count += 1
print(target)
