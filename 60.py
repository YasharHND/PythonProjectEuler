import math

primes = [3]


def is_prime(number):
    for i in range(3, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def next_prime():
    p1 = primes[-1]
    p2 = p1 + 2
    while not is_prime(p2):
        p2 += 2
    primes.append(p2)
    return p1


paths = []


def fits(prime, path):
    for item in path:
        if not is_prime(int(f"{prime}{item}")) or not is_prime(int(f"{item}{prime}")):
            return False
    return True


def find_matching_set(size):
    global paths
    while True:
        p = next_prime()
        for path in paths.copy():
            if fits(p, path):
                new_path = path + [p]
                if len(new_path) == size:
                    return new_path
                paths.append(new_path)
        paths.append([p])


matching_set = find_matching_set(5)
print(matching_set)
print(sum(matching_set))
