import math


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def quadratic(n, a, b):
    return (n ** 2) + (a * n) + b


max_count = 0
chosen_a = 0
chosen_b = 0
for a in range(-999, 1000, 2):
    for b in range(1, 1001, 2):
        if not is_prime(b):
            continue
        count = 0
        n = 0
        while True:
            q = quadratic(n, a, b)
            if q >= 2 and is_prime(q):
                count += 1
            else:
                break
            n += 1
        if count > max_count:
            max_count = count
            chosen_a = a
            chosen_b = b

print(chosen_a * chosen_b)
