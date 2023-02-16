import math


def distinct_prime_factors(n):
    out = set()
    if n % 2 == 0:
        out.add(2)
    while n % 2 == 0:
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            out.add(i)
            n = n / i
    if n > 2:
        out.add(int(n))
    return out


target = []
k = 1
while True:
    if len(distinct_prime_factors(k)) == 4:
        target.append(k)
        if len(target) == 4:
            print(target[0])
            break
    else:
        target.clear()
    k += 1
