import time
from functools import reduce


def pythagorean_triplet(m, n):
    return m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2


def solve():
    m = 2
    while True:
        for n in range(1, m):
            triplet = pythagorean_triplet(m, n)
            if sum(triplet) == 1000:
                return reduce(lambda x, y: x * y, triplet)
        m += 1


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
