from modules.primes import is_prime


def all_prime(number):
    str_number = str(number)
    return all(is_prime(int(str_number[i:])) and is_prime(int(str_number[:-i])) for i in range(1, len(str_number)))


summation = 0
n = 11
prime_count = 0
while prime_count < 11:
    if is_prime(n) and all_prime(n):
        prime_count += 1
        summation += n
    n += 1
print(summation)
