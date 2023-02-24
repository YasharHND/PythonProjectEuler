import time

from modules.numbers import continued_fraction, normal_fraction, is_perfect_square


def x_diophantine(d):
    cf = continued_fraction(d)
    fraction = normal_fraction(cf)
    x, y = fraction.denominator, fraction.numerator
    if len(cf.period) % 2 != 0:
        x, y = 2 * (x ** 2) + 1, 2 * x * y
    return x


def solve():
    target_d = 0
    maximum = 0
    for d in range(2, 1001):
        if is_perfect_square(d):
            continue
        x = x_diophantine(d)
        if x > maximum:
            target_d = d
            maximum = x
    return target_d


srt = time.time()
answer = solve()
end = time.time()
print(f"Answer: {answer}")
print(f"Time: {end - srt}")
