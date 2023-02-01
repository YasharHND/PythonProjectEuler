import math

# we need only odd_primes
primes = [3]


def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    for i in range(primes[-1] + 2, n, 2):
        if is_prime(i):
            primes.append(i)


def is_sum_a_prime_and_twice_a_square(n):
    for p in primes:
        r = (n - p) // 2
        if r == math.isqrt(r) ** 2:
            return True
    return False


k = 35
while True:
    if is_prime(k):
        primes.append(k)
    else:
        generate_primes(k)
        if not is_sum_a_prime_and_twice_a_square(k):
            print(k)
            break
    k += 2
