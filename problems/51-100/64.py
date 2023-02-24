import time

from modules.numbers import is_perfect_square, continued_fraction


def solve():
    summation = 0
    for i in range(2, 10_000):
        if is_perfect_square(i):
            continue
        if len(continued_fraction(i).period) % 2 == 1:
            summation += 1
    return summation


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
