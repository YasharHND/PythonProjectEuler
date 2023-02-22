from modules.primes import is_prime

n = 2
prime_count = 1
while prime_count < 10001:
    n += 1
    if is_prime(n):
        prime_count += 1
print(n)
