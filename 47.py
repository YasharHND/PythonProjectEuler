from primes import distinct_prime_factors

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
