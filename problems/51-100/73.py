import math
import time


def count_fractions(d):
    lower_limit = math.ceil(d / 3)
    if lower_limit <= 1:
        return 0
    upper_limit = math.floor(d / 2)
    count = 0
    for n in range(lower_limit, upper_limit + 1):
        if math.gcd(n, d) == 1:
            count += 1
    return count


def solve(limit):
    return sum(count_fractions(d) for d in range(2, limit + 1))


srt = time.time()
answer = solve(12000)
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt:.3f}")
