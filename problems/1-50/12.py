import math
import time


def divisors_count(number):
    count = 0
    for i in range(1, math.isqrt(number) + 1):
        if number % i == 0:
            count += 1 if number // i == i else 2
    return count


def solve():
    triangle = 1
    step = 2
    while True:
        if divisors_count(triangle) > 500:
            return triangle
        triangle += step
        step += 1


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
