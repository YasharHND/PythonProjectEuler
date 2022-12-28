def sum_of_divisors(n):
    return 1 + sum([k for k in range(2, (n // 2) + 1) if n % k == 0])


def is_abundant(n):
    return sum_of_divisors(n) > n


limit = 28123
to_be_deducted = set()
abundant_numbers = []
for number in range(1, limit):
    if is_abundant(number):
        abundant_numbers.append(number)
        abundant_numbers.sort()
        for an in abundant_numbers:
            summation = an + number
            if summation >= limit:
                break
            to_be_deducted.add(summation)
print(sum(range(1, limit)) - sum(to_be_deducted))
