import math
import time

from modules.numbers import is_perfect_square


class SequenceItem:
    def __init__(self, a_term, reminder):
        self.a_term = a_term
        self.reminder = reminder


def period_length(number):
    count = 0
    root = math.sqrt(number)
    floored_root = math.floor(root)
    first_item = last_item = SequenceItem(floored_root, [-1 * floored_root, 1])
    while True:
        count += 1
        denominator = number - last_item.reminder[0] ** 2
        gcd = abs(math.gcd(last_item.reminder[1], denominator))
        denominator //= gcd
        numerator = -1 * last_item.reminder[0] * (last_item.reminder[1] // gcd)
        a_term = math.floor((root + numerator) / denominator)
        numerator -= a_term * denominator
        last_item = SequenceItem(a_term, [numerator, denominator])
        if last_item.reminder == first_item.reminder:
            return count


def solve():
    summation = 0
    for i in range(2, 10_000):
        if is_perfect_square(i):
            continue
        if period_length(i) % 2 == 1:
            summation += 1
    return summation


srt = time.time()
answer = solve()
end = time.time()
print(answer)
print(f"Took {end - srt} seconds to execute...")
