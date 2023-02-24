import math
from fractions import Fraction
from functools import reduce


def divisors_sum(number):
    return 1 + sum([k for k in range(2, (number // 2) + 1) if number % k == 0])


def factorial(number):
    return reduce(lambda x, y: x * y, [i for i in range(1, number + 1)]) if number > 0 else 1


def is_perfect_square(number):
    return number ** 0.5 % 1 == 0


class ContinuedFractionSequenceItem:
    def __init__(self, a_term, reminder):
        self.a_term = a_term
        self.reminder = reminder


class ContinuedFraction:
    def __init__(self, a0, period):
        self.a0 = a0
        self.period = period


def continued_fraction(number):
    period = []
    root = math.sqrt(number)
    floored_root = math.floor(root)
    first_item = last_item = ContinuedFractionSequenceItem(floored_root, [-1 * floored_root, 1])
    while True:
        denominator = number - last_item.reminder[0] ** 2
        gcd = abs(math.gcd(last_item.reminder[1], denominator))
        denominator //= gcd
        numerator = -1 * last_item.reminder[0] * (last_item.reminder[1] // gcd)
        a_term = math.floor((root + numerator) / denominator)
        numerator -= a_term * denominator
        last_item = ContinuedFractionSequenceItem(a_term, [numerator, denominator])
        period.append(last_item.a_term)
        if last_item.reminder == first_item.reminder:
            return ContinuedFraction(first_item.a_term, period)


def normal_fraction(cf):
    target = [cf.a0] + cf.period[:-1]
    numerator = 1
    denominator = target.pop()
    while target:
        denominator, numerator = (denominator * target.pop()) + numerator, denominator
    return Fraction(numerator, denominator)
