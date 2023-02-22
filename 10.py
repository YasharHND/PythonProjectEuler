import time

from primes import is_prime


def solve():
    return 2 + sum(i for i in range(3, 2_000_000, 2) if is_prime(i))


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
