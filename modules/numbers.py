from functools import reduce


def divisors_sum(number):
    return 1 + sum([k for k in range(2, (number // 2) + 1) if number % k == 0])


def factorial(number):
    return reduce(lambda x, y: x * y, [i for i in range(1, number + 1)]) if number > 0 else 1


def is_perfect_square(number):
    return number ** 0.5 % 1 == 0
